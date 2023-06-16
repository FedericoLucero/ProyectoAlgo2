import variety_functions
import argparse
import domain
import graphic_interface

# Definimos las variables para la persistencia de los datos

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

    variety_functions.open_file_dump("uberMap.pickle", "wb", uberMap) # guarda
    variety_functions.open_file_dump("fixUbications.pickle", "wb", dict()) # guarda
    variety_functions.open_file_dump("mobileUbications.pickle", "wb", dict()) # guarda
    
    if uberMap != None:
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

    fixElement = domain.FixUbication()
    fixElement = variety_functions.create_fix_mobil_ubication(fixElement, direccion)

    grafo = variety_functions.open_file_load("uberMap.pickle","rb") # carga 
    fixUbications = variety_functions.open_file_load("fixUbications.pickle","rb") # carga

    Aristas = variety_functions.open_file_load("Aristas.pickle","rb") # carga

    error = variety_functions.load_fix_element(fixElement, grafo, fixUbications, nombre, Aristas) # retorna string o None
    if error != None:
        print(error)
        return
    
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

    mobilElement = domain.MobileUbication()
    mobilElement.Amount = int(monto)
    mobilElement = variety_functions.create_fix_mobil_ubication(mobilElement, direccion)

    mobileUbications = variety_functions.open_file_load("mobileUbications.pickle","rb") # carga
   
    Aristas = variety_functions.open_file_load("Aristas.pickle", "rb") # carga

    error = variety_functions.load_mobil_element(mobilElement, mobileUbications, nombre, Aristas) # retorna string o None
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
        
        grafo = variety_functions.open_file_load("uberMap.pickle","rb") # carga 
        fixUbications = variety_functions.open_file_load("fixUbications.pickle","rb") # carga
        mobileUbications = variety_functions.open_file_load("mobileUbications.pickle","rb") # carga


        print("Persona: ",persona, ". Viaje hasta:",direccion_elemento)
        distanceToDestiny = 0
        destiny = ""
        origin = ""
        if len(direccion_elemento)>3: #Analiza si es una ubicacion (no mayor que 3 digitos) o  una direccion 
            destUbi = variety_functions.create_address(direccion_elemento)
            destiny = destUbi[1][0]
            distanceToDestiny = destUbi[1][1]
            origin = destUbi[0][0]
        else:
            destiny = fixUbications[direccion_elemento].Address.CornerDestiny.Name
            origin = fixUbications[direccion_elemento].Address.CornerOrigin.Name
            distanceToDestiny = fixUbications[direccion_elemento].Address.CornerDestiny.DistantTo
            
        error = variety_functions.check_person_action(persona, mobileUbications, grafo, destiny,distanceToDestiny,origin)
        if error != None:
            print(error)
            return
        
        nearestCars = variety_functions.find_nearests_3cars(persona, mobileUbications, grafo)
        if len(nearestCars) == 0:
            print ("No hay vehiculos disponibles por tu monto actual o por que se encuentran inhabilitados")
            return
        
        personDestiny = mobileUbications[persona].Address.CornerDestiny.Name
        
        i = graphic_interface.exec(nearestCars,persona,mobileUbications[persona].Amount)
        if i == 0:
            print("No se seleccionó ningun auto")
            return
        i-=1
 
        print("Camino mas corto: ",variety_functions.find_path(grafo, personDestiny, destiny,origin))

        variety_functions.move_mobile_elements(mobileUbications,persona,nearestCars[i][0],nearestCars[i][1],direccion_elemento,fixUbications)
        variety_functions.print_ubications(mobileUbications)

        variety_functions.open_file_dump("mobileUbications.pickle", "wb", mobileUbications) # guarda

def reset_all():
    variety_functions.open_file_dump("Vertices.pickle", "wb", "")
    variety_functions.open_file_dump("Aristas.pickle", "wb", "")
    variety_functions.open_file_dump("uberMap.pickle", "wb", "")
    variety_functions.open_file_dump("fixUbications.pickle", "wb", "")
    variety_functions.open_file_dump("mobileUbications.pickle", "wb", "")
    
def print_graph():
    uberMap = variety_functions.open_file_load("uberMap.pickle", "rb")
    variety_functions.print_all_nodes(uberMap)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-create_map", type=str, help="Crear un mapa utilizando el local_path")
    parser.add_argument("-load_fix_element", nargs=2, metavar=("nombre", "direccion"), help="Cargar un elemento fijo en el mapa")
    parser.add_argument("-load_movil_element", nargs=3, metavar=("nombre", "direccion", "monto"), help="Cargar un elemento móvil en el mapa")
    parser.add_argument("-create_trip", nargs=2, metavar=("persona", "direccion/elemento"), help="Crear un viaje")
    parser.add_argument("-reset_all", action="store_true", help="Resetear todos los archivos")
    parser.add_argument("-print_graph", action="store_true", help="Imprimir grafo")
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
    if args.print_graph:
        print_graph()


    # Crea mapa
    create_map("local_path_original.txt")

    load_fix_element("H1", "<e4,5> <e8,5>") 
    load_fix_element("A1", "<e5,5> <e1,5>") 
    load_fix_element("T5", "<e14,8> <e13,0>") 
    load_fix_element("H4", "<e9,0> <e10,4>") 
    load_fix_element("S10", "<e12,3> <e16,3>") 
    load_fix_element("K1", "<e12,3> <e16,3>") 
    
    load_movil_element( "P1","<e3,3> <e4,3>" ,20000)
    load_movil_element( "P2","<e9,0> <e10,4>" ,40000)
    load_movil_element( "P3","<e14,8> <e13,8>" ,2500)
    load_movil_element( "P4","<e7,50> <e11,50>" ,0)
    load_movil_element( "C1","<e7,0> <e6,4>" ,200)
    load_movil_element( "C2", "<e9,0> <e10,4>" ,0)
    load_movil_element( "C3", "<e7,49> <e11,51>" ,50)
    
    create_trip("P1", "<e3,2> <e8,3>")
    create_trip("P1", "<e11,2> <e12,2>")
    create_trip("P1", "<e15,1> <e16,1>")
    create_trip("P2", "H4")
    create_trip("P2", "<e7,50> <e11,50>")
    create_trip("P3", "S10")
    create_trip("P4", "<e7,100> <e11,0>")
