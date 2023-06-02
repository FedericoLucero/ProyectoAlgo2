import argparse
import pickle
import re
info = {}
grafo = {}
#
def create_map(local_path):
    """ Código para crear el mapa utilizando el local_path """
    
    archivo = open(local_path) # Abre el archivo en modo lectura ("r")
    try:
        linea1 = archivo.readline() # El puntero se actualiza
        linea2 = archivo.readline() # El puntero se actualiza
    finally:
        archivo.close() # Cierra el archivo después de haberlo utilizado

    vertices = [v for v in re.findall(r'(e\d+)', linea1)] # Extraer "e" seguido de los dígitos como una cadena de texto
    
    valores = re.findall(r'(e\d+),(e\d+),(\d+)', linea2) # Extraer "e" seguido de los dígitos como una cadena de texto en la 3-tupla
    Aristas = [(v[0], v[1], int(v[2])) for v in valores] # Convertir los valores en una lista de tuplas

    for vertice in vertices: # Recorre cada vertice
        grafo[vertice] = {} # Agregar vertices al grafo
    
    for arista in Aristas: # recorre cada arista
        origen, destino, distancia = arista
        grafo[origen][destino] = distancia # Agrega aristas al grafo

    with open("grafo.pickle", "wb") as archivo: # Utiliza "with open" para abrir el archivo en modo de escritura binaria ("wb")
        pickle.dump(grafo, archivo) # Utilizar pickle para escribir el objeto "grafo" en el archivo

    with open("info.pickle", "wb") as archivo: # Utiliza "with open" para abrir el archivo en modo de escritura binaria ("wb")
        pickle.dump(info, archivo) # Utilizar pickle para escribir el objeto "info" en el archivo

    print(f"Se ha creado el mapa utilizando el local_path: {local_path}")
    return grafo
  
def load_fix_element(nombre, direccion):
    """ Implementa la lógica para cargar un elemento fijo en el mapa utilizcmando <nombre> y <direccion> """

    valores = re.findall(r'(e\d+),(\d+),(e\d+),(\d+)', direccion)  # Extraee "e" seguido de los dígitos como una cadena de texto 
    Direccion = [((valores[0][0]), int(valores[0][1])), ((valores[0][2]), int(valores[0][3]))] # Convertir los valores extraídos en una lista de dos tuplas, con el primer elemento como cadena de texto y el segundo como entero
    
    with open("info.pickle", "rb") as f: # Abre el archivo "info.pickle" en modo de lectura binaria ("rb")
        info = pickle.load(f) # Cargar el contenido del archivo en la variable "info"

        if nombre not in info: # Verificar si el nombre no está en el diccionario "info"
            info[nombre] = Direccion 
            with open("info.pickle", "wb") as f: # Abrir el archivo "info.pickle" en modo de escritura binaria ("wb")
                pickle.dump(info, f) # Guardar el diccionario actualizado en el archivo

            print(f"Se ha cargado un elemento fijo {nombre} en el mapa en la dirección {direccion}")
        else:
            print(f"El elemento fijo {nombre} ya existe en el mapa en la dirección {direccion}")

def load_movil_element(nombre, direccion, monto):
    """ Implementa la lógica para cargar un elemento móvil en el mapa utilizando <nombre>, <direccion> y <monto> """
    
    valores = re.findall(r'(e\d+),(\d+),(e\d+),(\d+)', direccion)  # Extraee "e" seguido de los dígitos como una cadena de texto 
    Direccion = [((valores[0][0]), int(valores[0][1])), ((valores[0][2]), int(valores[0][3]))] # Convertir los valores extraídos en una lista de dos tuplas, con el primer elemento como cadena de texto y el segundo como entero

    with open("info.pickle", "rb") as f: # Abre el archivo "info.pickle" en modo de lectura binaria ("rb")
        info = pickle.load(f) # Cargar el contenido del archivo en la variable "info"

        if nombre not in info: # Verificar si el nombre no está en el diccionario "info"
            info[nombre] = (Direccion,monto) 
            with open("info.pickle", "wb") as f: # Abrir el archivo "info.pickle" en modo de escritura binaria ("wb")
                pickle.dump(info, f) # Guarda el diccionario actualizado en el archivo

            print(f"Se ha cargado un elemento móvil {nombre} en el mapa en la dirección {direccion} con un monto de {monto}")
        else:
            print(f"El elemento movil {nombre} ya existe en el mapa, en la dirección {direccion}")

def create_trip(persona, direccion_elemento):
    """ Implementa la lógica para crear un viaje utilizando <persona> y <direccion_elemento> """

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