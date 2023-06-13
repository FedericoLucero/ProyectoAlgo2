import variety_functions
import diccionary
import argparse
import domain
import graphic_interface

grafo = dict() #definimos la variable grafo para la persistencia de los datos

fixUbications = dict()

mobileUbications = dict()

selectCar = None
""" 
def create_map(local_path):
Descripcion: Código para crear el mapa utilizando el local_path
Herraminetas/Estructuras usadas:
{ Grafo(Diccionario de Diccionarios),
  Ubicaciones(Hash Table),
  ¿Direcciones()?,
  ¿Distancias_caminos(Diccionario)? }
""" 
#
def create_map(local_path):
    
    line1, line2 = variety_functions.read_lines(local_path)
    Vertices, Aristas = variety_functions.Create_V_A(line1,line2) # Listas de [vertices] y [Aristas]

    #Grafo = graph.createGraph(Vertices,Aristas) 
    #graph.printGraph(Grafo)     #eliminar
    #Ubicaciones = diccionary.createDiccionary(26)
    #diccionary.printHashtable(Ubicaciones)     #eliminar

    #Direcciones = blabla.create...() # (?????
    #print(Direcciones)     #eliminar
    #Distancias_caminos = blabla.create...() # dicicionario de python(?????
    #print(Distancias_caminos)     #eliminar
    uberMap = variety_functions.create_map_dictionary(Vertices,Aristas)
    ubications = dict()


    global grafo
    grafo = uberMap
    variety_functions.open_file_dump("uberMap.pickle", "wb",uberMap)
    variety_functions.open_file_dump("ubications.pickle", "wb",ubications)
    
    # variety_functions.open_file_dump("Ubicaciones.pickle", "wb",Ubicaciones)
    #variety_functions.open_file_dump("Direcciones.pickle", "wb",Direcciones)
    #variety_functions.open_file_dump("Distancias_caminos.pickle", "wb",Distancias_caminos)
    if uberMap != None:
        #variety_functions.print_all_nodes(uberMap)
        print("map created successfully")
    else:
        print("ocurrio un error creando el mapa")

        

""" 
def load_fix_element(nombre, direccion):
Descripcion: Codigo para cargar un elemento fijo en el mapa utilizcmando <nombre> y <direccion>
Herraminetas/Estructuras usadas:
{ clase(fix_element),
  Ubicaciones(Hash Table), }
"""

def load_fix_element(nombre, direccion):
    
    global grafo
    global fixUbications

    Direccion = variety_functions.create_address(direccion) # Lista de un par de tuplas [(,),(,)]
    
    fixElement = domain.FixUbication()
    
    address = domain.Address()
    
    cornerOrigin = domain.Corner()
    cornerDestiny = domain.Corner()
    
    cornerOrigin.Name = Direccion[0][0]
    cornerOrigin.DistantTo = Direccion[0][1]
    
    cornerDestiny.Name = Direccion[1][0]
    cornerDestiny.DistantTo = Direccion[1][1]
    
    address.CornerDestiny = cornerDestiny 
    address.CornerOrigin = cornerOrigin
    
    fixElement.Address=address
    line1, line2 = variety_functions.read_lines("local_path_original.txt")#esto se cambia por el picke
    Vertices, Aristas = variety_functions.Create_V_A(line1,line2) #esto se cambia por el picke
    error = variety_functions.load_fix_element(fixElement,grafo,fixUbications,nombre,Aristas)
    print("loading:",nombre,error)
    variety_functions.print_all_nodes(grafo)
    variety_functions.print_ubications(fixUbications)
    #Ubicaciones = variety_functions.open_file_load("Ubicaciones.pickle","rb") # Carga el contenido del archivo en la variable "Ubicaciones"
    #diccionary.printHashtable(Ubicaciones)     #eliminar

""" 
def load_movil_element(nombre, direccion, monto):
Descripcion: Codigo para cargar un elemento movil en el mapa utilizcmando <nombre>, <direccion> y <monto>
Herraminetas/Estructuras usadas:
{ clase(fix_element),
  Ubicaciones(Hash Table), }
"""

def load_movil_element(nombre, direccion, monto):
    ubicationName = nombre
    Direccion = variety_functions.create_address(direccion) # Lista de un par de tuplas [(,),(,)]

    element = domain.MobileUbication() # clase
    element.Amount = int(monto)

    cornerOrigin = domain.Corner()
    cornerDestiny = domain.Corner()

    cornerOrigin.Name = Direccion[0][0]
    cornerOrigin.DistantTo = Direccion[0][1]
    
    cornerDestiny.Name = Direccion[1][0]
    cornerDestiny.DistantTo = Direccion[1][1]

    Address = domain.Address()
    Address.CornerOrigin = cornerOrigin
    Address.CornerDestiny = cornerDestiny

    element.Address = Address

    uberMap = variety_functions.open_file_load("uberMap.pickle","rb") # Carga el contenido del archivo en la variable "uberMap"
    
    ubications = variety_functions.open_file_load("ubications.pickle","rb") # Carga el contenido del archivo en la variable "ubications"
    global mobileUbications
    ubications = mobileUbications
    line1, line2 = variety_functions.read_lines("local_path_original.txt") #esto se cambia por el picke
    Vertices, Aristas = variety_functions.Create_V_A(line1,line2) #esto se cambia por el picke
    print(variety_functions.check_element(ubicationName, element, Aristas, ubications))


    if variety_functions.check_element(ubicationName, element, Aristas, ubications) == None: # Serie de condiciones a cumplir
        ubications[nombre] = element   
        mobileUbications = ubications
        variety_functions.open_file_dump("ubications.pickle","wb",ubications) # Guarda el contenido de la variable "Ubicaciones" en el archivo
        print(f"Se ha cargado un elemento móvil {nombre} en el mapa en la dirección {direccion} con un monto de {monto}")

    #diccionary.printHashtable(Ubicaciones)     #eliminar

#def load_movil(mobilElement: domain.mobilUbication, uberMap: dict(),mobilUbications: dict()):
  #print("a")

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
        
        destiny = direccion_elemento
        if len(direccion_elemento)>3:
            destUbi = variety_functions.create_address(direccion_elemento)
            destiny = destUbi[1][0]

        
        error= variety_functions.check_person_action(persona,mobileUbications,grafo,direccion_elemento)
        if error != None:
            print(error)
            return
        
        nearestCars = variety_functions.find_nearests_3cars(persona,mobileUbications,grafo)

        global selectCar
        print(nearestCars)
        if len(nearestCars)==0:
            print ("No hay autos disponibles para tu monto actual")
            return
        
        origin = mobileUbications[persona].Address.CornerOrigin.Name
        print(variety_functions.find_path(grafo,origin,direccion_elemento))
        
        i=graphic_interface.exec(nearestCars)
        if i == 0:
            print("no se seleccionó ningun auto")
            return
        i-=1
        print(i)
        variety_functions.move_mobile_elements(mobileUbications,persona,nearestCars[i][0],nearestCars[i][1],destiny,fixUbications)

        variety_functions.print_ubications(mobileUbications)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-create_map", type=str, help="Crear un mapa utilizando el local_path")
    parser.add_argument("-load_fix_element", nargs=2, metavar=("nombre", "direccion"), help="Cargar un elemento fijo en el mapa")
    parser.add_argument("-load_movil_element", nargs=3, metavar=("nombre", "direccion", "monto"), help="Cargar un elemento móvil en el mapa")
    parser.add_argument("-create_trip", nargs=2, metavar=("persona", "direccion/elemento"), help="Crear un viaje")
    args = parser.parse_args()

    if args.create_map:
        create_map(args.create_map)
    if args.load_fix_element:
        load_fix_element(*args.load_fix_element)
    if args.load_movil_element:
        load_movil_element(*args.load_movil_element)
    if args.create_trip:
        create_trip(*args.create_trip)
    
    
    create_map("local_path_original.txt")
    # Direcciones fijas
    load_fix_element( "H4", "<e14,3>,<e13,5>")
    load_fix_element( "H1", "<e2,2>,<e3,2>")
    load_fix_element( "A1", "<e12,1>,<e16,5>")
    load_fix_element( "T5", "<e1,10>,<e5,0>")
    load_fix_element( "S10", "<e9,2>,<e10,2>")
    load_fix_element( "SF2", "<e3,2>,<e11,2>")
    

    load_movil_element("P1", "<e10,4>,<e11,4>", "2000")
    load_movil_element("P2", "<e11,0>,<e7,100>", "4000")
    load_movil_element("P3", "<e15,2>,<e11,4>", "2500")
    load_movil_element("P4", "<e4,5>,<e8,5>", "50")
    load_movil_element("C1", "<e14,2>,<e13,6>", "200")
    load_movil_element("C2", "<e1,2>,<e2,2>", "50")
    load_movil_element("C3", "<e3,4>,<e7,4>", "110")
    load_movil_element("C4", "<e9,1>,<e10,3>", "20")
    load_movil_element("C5", "<e7,50>,<e11,50>", "25")

    create_trip("P1", "H4")
    create_trip("P5" ,"<e3,10>,<e2,40>")
    create_trip("P3" ,"H1")
    create_trip("P4" ,"<e8,5>,<e4,5>")
    create_trip("P1" ,"A1")
    #create_trip ("P2" ,"<e9,50> <e10,0>")