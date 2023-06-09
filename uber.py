import variety_functions
import diccionary
import argparse
import domain

grafo = dict() #definimos la variable grafo para la persistencia de los datos

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
    uberMap =  variety_functions.create_map_dictionary(Vertices,Aristas)
    grafo = uberMap
            
    # variety_functions.open_file_dump("Grafo.pickle", "wb",Grafo)
    # variety_functions.open_file_dump("Ubicaciones.pickle", "wb",Ubicaciones)
    #variety_functions.open_file_dump("Direcciones.pickle", "wb",Direcciones)
    #variety_functions.open_file_dump("Distancias_caminos.pickle", "wb",Distancias_caminos)
    if uberMap != None:
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

    f_element = variety_functions.fix_element() # clase
    Direccion = variety_functions.create_address(direccion) # Lista de un par de tuplas [(,),(,)]
    
    Ubicaciones = variety_functions.open_file_load("Ubicaciones.pickle","rb") # Carga el contenido del archivo en la variable "Ubicaciones"
        
    if variety_functions.check_element(Ubicaciones, nombre) == True: # Serie de condiciones a cumplir
        f_element.nombre = nombre
        f_element.direccion = Direccion
        diccionary.insert(Ubicaciones, nombre, f_element) # insert(Hash Table, key, elemento)
        
        variety_functions.open_file_dump("Ubicaciones.pickle","wb",Ubicaciones) # Guarda el contenido de la variable "Ubicaciones" en el archivo
        print(f"Se ha cargado un elemento fijo {nombre} en el mapa en la dirección {direccion}")
    else:
        print(f"El elemento fijo {nombre} ya existe en el mapa en la dirección {direccion}")
    #diccionary.printHashtable(Ubicaciones)     #eliminar

""" 
def load_movil_element(nombre, direccion, monto):
Descripcion: Codigo para cargar un elemento movil en el mapa utilizcmando <nombre>, <direccion> y <monto>
Herraminetas/Estructuras usadas:
{ clase(fix_element),
  Ubicaciones(Hash Table), }
"""

def load_movil_element(nombre, direccion, monto):
    
    m_element = variety_functions.movil_element() # clase
    Direccion = variety_functions.create_address(direccion) # Lista de un par de tuplas [(,),(,)]
    
    Ubicaciones = variety_functions.open_file_load("Ubicaciones.pickle","rb") # Carga el contenido del archivo en la variable "Ubicaciones"
        
    if variety_functions.check_element(Ubicaciones,nombre) == True: # Serie de condiciones a cumplir
        m_element.nombre = nombre
        m_element.direccion = Direccion
        m_element.monto = int(monto)
        diccionary.insert(Ubicaciones,nombre,m_element) # insert(Hash Table, key, elemento)
        
        variety_functions.open_file_dump("Ubicaciones.pickle","wb",Ubicaciones) # Guarda el contenido de la variable "Ubicaciones" en el archivo
        print(f"Se ha cargado un elemento móvil {nombre} en el mapa en la dirección {direccion} con un monto de {monto}")
    else:
        print(f"El elemento movil {nombre} ya existe en el mapa, en la dirección {direccion}")
    #diccionary.printHashtable(Ubicaciones)     #eliminar

""" 
def create_trip(persona, direccion_elemento):
Descripcion: para crear un viaje utilizando <persona> y <direccion_elemento>
Herraminetas/Estructuras usadas:
{}
"""

def create_trip(persona, direccion_elemento):
    #chequear que la persona exista
    #chequear si ha ingresado una direccion {(ex,int),(ey,int)} o un elemento ej: H1
    print(f"Se ha creado un viaje para {persona} hacia {direccion_elemento}")

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
