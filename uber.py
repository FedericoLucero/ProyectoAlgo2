import variety_functions
import diccionary
import argparse
import domain
import graphic_interface

# Definimos las variables para la persistencia de los datos
grafo = dict() 
fixUbications = dict()
mobileUbications = dict()
selectCar = None

""" 
def create_map(local_path):
Descripcion: Código para crear el mapa utilizando el local_path
Entrada: local_path.txt
Herraminetas/Estructuras usadas:
{ grafo(Diccionary de python de Diccionary de python) }
""" 

def create_map(local_path):
    
    line1, line2 = variety_functions.read_lines(local_path) # retorna dos strings
    Vertices, Aristas = variety_functions.Create_V_A(line1, line2) # retorna dos listas
    variety_functions.open_file_dump("Vertices.pickle", "wb", Vertices) # guarda
    variety_functions.open_file_dump("Aristas.pickle", "wb", Aristas) # guarda

    uberMap = variety_functions.create_map_dictionary(Vertices, Aristas) # retorna diccionary

    global grafo
    grafo = uberMap
    variety_functions.open_file_dump("uberMap.pickle", "wb", uberMap) # guarda
    variety_functions.open_file_dump("fixUbications.pickle", "wb", fixUbications) # guarda
    variety_functions.open_file_dump("mobileUbications.pickle", "wb", mobileUbications) # guarda
    
    if uberMap != None:
        variety_functions.print_all_nodes(uberMap)
        print("mapa creado con exito")
    else:
        print("ocurrio un error creando el mapa")

""" 
def load_fix_element(nombre, direccion):
Descripcion: Codigo para cargar un elemento fijo en el mapa utilizcmando <nombre> y <direccion>
Herraminetas/Estructuras usadas:
{  }
"""

def load_fix_element(nombre, direccion):
    nombre = str(nombre)

    global grafo
    global fixUbications

    fixElement = domain.FixUbication()
    fixElement = variety_functions.create_fix_mobil_ubication(fixElement, direccion)

    grafo = variety_functions.open_file_load("uberMap.pickle","rb") # carga 
    fixUbications = variety_functions.open_file_load("fixUbications.pickle","rb") # carga

    Vertices = variety_functions.open_file_load("Vertices.pickle","rb") # carga 
    Aristas = variety_functions.open_file_load("Aristas.pickle","rb") # carga

    error = variety_functions.load_fix_element(fixElement, grafo, fixUbications, nombre, Aristas) # retorna string o None
    print("loading:",nombre,error)
    #variety_functions.print_all_nodes(grafo)
    variety_functions.print_ubications(fixUbications)

    if error == None:
        variety_functions.open_file_dump("fixUbications.pickle", "wb", fixUbications) # guarda
        variety_functions.open_file_dump("uberMap.pickle", "wb", grafo) # guarda

""" 
def load_movil_element(nombre, direccion, monto):
Descripcion: Codigo para cargar un elemento movil en el mapa utilizcmando <nombre>, <direccion> y <monto>
Herraminetas/Estructuras usadas:
{  }
"""

def load_movil_element(nombre, direccion, monto):

    global grafo
    global mobileUbications

    mobilElement = domain.MobileUbication()
    mobilElement.Amount = int(monto)
    mobilElement = variety_functions.create_fix_mobil_ubication(mobilElement, direccion)

    mobileUbications = variety_functions.open_file_load("mobileUbications.pickle","rb") # carga

    Vertices = variety_functions.open_file_load("Vertices.pickle", "rb") # carga
    Aristas = variety_functions.open_file_load("Aristas.pickle", "rb") # carga

    error = variety_functions.load_mobil_element(mobilElement, grafo, mobileUbications, nombre, Aristas) # retorna string o None
    print("loading:",nombre, error)
    #variety_functions.print_all_nodes(grafo)
    variety_functions.print_ubications(mobileUbications)
    if error == None:
        variety_functions.open_file_dump("mobileUbications.pickle", "wb", mobileUbications) # guarda

""" 
def create_trip(persona, direccion_elemento):
Descripcion: para crear un viaje utilizando <persona> y <direccion_elemento>
Herraminetas/Estructuras usadas:
{}
"""

def create_trip(persona, direccion_elemento):
        global grafo
        global mobileUbications
        global fixUbications
        
        grafo = variety_functions.open_file_load("uberMap.pickle","rb") # carga 
        fixUbications = variety_functions.open_file_load("fixUbications.pickle","rb") # carga
        mobileUbications = variety_functions.open_file_load("mobileUbications.pickle","rb") # carga

        destiny = direccion_elemento
        if len(direccion_elemento)>3:
            destUbi = variety_functions.create_address(direccion_elemento)
            destiny = destUbi[1][0]

        error = variety_functions.check_person_action(persona, mobileUbications, grafo, direccion_elemento)
        if error != None:
            print(error)
            return
        
        nearestCars = variety_functions.find_nearests_3cars(persona, mobileUbications, grafo)

        global selectCar
        print(nearestCars)
        if len(nearestCars) == 0:
            print ("No hay autos disponibles para tu monto actual")
            return
        
        origin = mobileUbications[persona].Address.CornerOrigin.Name
        print(variety_functions.find_path(grafo, origin, direccion_elemento))
        
        i = graphic_interface.exec(nearestCars)
        if i == 0:
            print("no se seleccionó ningun auto")
            return
        i-=1
        print(i)

        variety_functions.move_mobile_elements(mobileUbications,persona,nearestCars[i][0],nearestCars[i][1],destiny,fixUbications)
        variety_functions.print_ubications(mobileUbications)

        variety_functions.open_file_dump("mobileUbications.pickle", "wb", mobileUbications) # guarda

def reset_all():
    variety_functions.open_file_dump("Vertices.pickle", "wb", "")
    variety_functions.open_file_dump("Aristas.pickle", "wb", "")
    variety_functions.open_file_dump("uberMap.pickle", "wb", "")
    variety_functions.open_file_dump("fixUbications.pickle", "wb", "")
    variety_functions.open_file_dump("mobileUbications.pickle", "wb", "")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-create_map", type=str, help="Crear un mapa utilizando el local_path")
    parser.add_argument("-load_fix_element", nargs=2, metavar=("nombre", "direccion"), help="Cargar un elemento fijo en el mapa")
    parser.add_argument("-load_movil_element", nargs=3, metavar=("nombre", "direccion", "monto"), help="Cargar un elemento móvil en el mapa")
    parser.add_argument("-create_trip", nargs=2, metavar=("persona", "direccion/elemento"), help="Crear un viaje")
    parser.add_argument("-reset_all", action="store_true", help="Resetear todos los archivos")
    args = parser.parse_args()

    if args.create_map:
        create_map(args.create_map)
    if args.load_fix_element:
        load_fix_element(*args.load_fix_element)
    if args.load_movil_element:
        load_movil_element(*args.load_movil_element)
    if args.create_trip:
        create_trip(*args.create_trip)
    if args.reset_all:
        reset_all()

    """
    # Crea mapa
    create_map("local_path_original.txt")

    # Direcciones fijas
    load_fix_element( "H4", "<e14,3>,<e13,5>")
    load_fix_element( "H1", "<e2,2>,<e3,2>")
    load_fix_element( "A1", "<e12,1>,<e16,5>")
    load_fix_element( "T5", "<e1,10>,<e5,0>")
    load_fix_element( "S10", "<e9,2>,<e10,2>")
    load_fix_element( "SF2", "<e3,2>,<e11,2>")
    
    # Direcciones moviles
    load_movil_element("P1", "<e10,4>,<e11,4>", "2000")
    load_movil_element("P2", "<e11,0>,<e7,100>", "4000")
    load_movil_element("P3", "<e15,2>,<e11,4>", "2500")
    load_movil_element("P4", "<e4,5>,<e8,5>", "50")
    load_movil_element("C1", "<e14,2>,<e13,6>", "200")
    load_movil_element("C2", "<e1,2>,<e2,2>", "50")
    load_movil_element("C3", "<e3,4>,<e7,4>", "110")
    load_movil_element("C4", "<e9,1>,<e10,3>", "20")
    load_movil_element("C5", "<e7,50>,<e11,50>", "25")

    # Crea Viaje
    create_trip("P1", "H4")
    create_trip("P5" ,"<e3,10>,<e2,40>")
    create_trip("P3" ,"H1")
    create_trip("P4" ,"<e8,5>,<e4,5>")
    create_trip("P1" ,"A1")
    #create_trip ("P2" ,"<e9,50> <e10,0>")
    """

    reset_all()