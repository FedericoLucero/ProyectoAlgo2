from uber import*
import pickle
import re

"""
Clases
"""

class fix_element():
    nombre = None
    direccion = None

class movil_element():
    nombre = None
    direccion = None
    monto = None

""" 
def read_lines(local_path):
Descripcion: lee la linea 1 y 2 del local_path devolviendo dos strings
"""
def read_lines(local_path):
    archive = open(local_path) # Abre el archivo en modo lectura ("r")
    try:
        line1 = archive.readline()
        line2 = archive.readline()
    finally:
        archive.close()
    return line1,line2

""" 
def Create_V_A(line1,line2):
Descripcion: lee los strings linea 1 y 2 convirtiendolos en dos listas
Salidas: 
{ Vertices = ["ex","ey","ez",...],
  Aristas = [("ex","ey",int),...] }
"""

def Create_V_A(line1,line2):
    Vertices = [v for v in re.findall(r'(e\d+)', line1)] # Extrae "e" seguido de los dígitos como un string

    valores = re.findall(r'(e\d+),(e\d+),(\d+)', line2) # Extraer "e" seguido de los dígitos como una cadena de texto en la 3-tupla
    Aristas = [(v[0], v[1], int(v[2])) for v in valores] # Convertir los valores en una lista de 3-tuplas
    return Vertices, Aristas

""" 
defcreate_address(direccion):
Descripcion: lee el strings ingresado como direccion y devuelve una lista de un par de tuplas
Salidas: 
{ direccion = [("ex",int),("ey",int)] }
"""

def create_address(direccion):
    valores = re.findall(r'(e\d+),(\d+),(e\d+),(\d+)', direccion)  # Extrae "e" seguido de los dígitos como una cadena de texto 
    Direccion = [((valores[0][0]), int(valores[0][1])), ((valores[0][2]), int(valores[0][3]))] # Convertir los valores extraídos en una lista de dos tuplas, con el primer elemento como cadena de texto y el segundo como entero
    return Direccion

""" 
def check_element(Ubicaciones,nombre):
Descripcion: comprueba una serie de condiciones para insertar el valor en el hash table
Salidas: 
{ True = cumple todas las condicones ,
  False = NO cumple al menos una condicon }
"""

def check_element(Ubicaciones,nombre):
    if diccionary.search(Ubicaciones,nombre) == None: # verifica si ya existe el nombre
        #if verificar que la direccion no este ocupada
            #if verificar que la direccion no tenga errores de dsitancia
                #if verifica que la direccion sea existente
                    return True
    return False

""" 
def open_file_load(archivo,modo):
Descripcion: Carga el contenido del archivo en una variable
Salidas: { variable }
"""

def open_file_load(archivo,modo):
    with open(archivo, modo) as f: # Abre el archivo en modo lectura 
        variable = pickle.load(f) # Cargar el contenido del archivo en la variable 
        return variable
    
""" 
def open_file_dump(archivo,modo,variable):
Descripcion: guarda el contenido de la variable en el archivo
"""

def open_file_dump(archivo,modo,variable):
    with open(archivo, modo) as f: # Abrir el archivo en modo de escritura
        pickle.dump(variable, f) # Guardar el contenido en el archivo
