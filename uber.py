import argparse
import graph
import re

def create_map(local_path): # Código para crear el mapa utilizando el local_path
    
    f = open(local_path)  # Abre el archivo en modo lectura ("r")
    try:
        linea1 = f.readline()  # El puntero se actualiza
        linea2 = f.readline()  # El puntero se actualiza
    finally:
        f.close()  # Cierra el archivo después de haberlo utilizado

    vertices = [int(v) for v in re.findall(r'e(\d+)', linea1)]  # Extraer los valores después de "e" como enteros

    valores = re.findall(r'e(\d+),e(\d+),(\d+)', linea2)  # Extraer los valores después de "e" en la 3-tupla
    Aristas_dis = [(int(v[0]), int(v[1]), int(v[2])) for v in valores]  # Convertir los valores en una lista de tuplas

    print(vertices)
    print(Aristas_dis)

    #graph.createGraph(vertices, Aristas_dis)
    
    print(f"Se ha creado el mapa utilizando el local_path: {local_path}")
  
def load_fix_element(nombre, direccion):
  # Implementa la lógica para cargar un elemento fijo en el mapa utilizando <nombre> y <direccion>
  print(f"Se ha cargado un elemento fijo {nombre} en el mapa en la dirección {direccion}")

def load_movil_element(nombre, direccion, monto):
  # Implementa la lógica para cargar un elemento móvil en el mapa utilizando <nombre>, <direccion> y <monto>
  print(f"Se ha cargado un elemento móvil {nombre} en el mapa en la dirección {direccion} con un monto de {monto}")

def create_trip(persona, direccion_elemento):
  # Implementa la lógica para crear un viaje utilizando <persona> y <direccion_elemento>
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