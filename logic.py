    print("aristas",Aristas)
    uberMap = dict() #defino el objeto como un dict vacio para poder acceder luego a todos los vertices -P
    for vertice in vertices: # Recorre cada vertice -F 
        grafo[vertice] = {} # Agregar vertices al grafo -F
        uberMap[vertice] = dict() #Defino cada vertice como un diccionario vacio para que  luego pueda acceder a "[origen][destino]" -P
        
    for arista in Aristas: # recorre cada arista -F 
        origen, destino, distancia = arista
        grafo[origen][destino] = distancia # Agrega aristas al grafo -F 
        newAddress = domain.Distance() #Genera objeto de tipo Distance -P
        newAddress.Distance=distancia #asigna el valor de distancia de la arista al dicho objeto -P 
        uberMap[origen][destino] = newAddress #genera  en la estuctura "ubermap" la arista correspondiente con las aristas "directas" -P
        
    for origin in uberMap: #recorre todos los vertices originales
        for newOrigin in uberMap: #por cada vez que se recorren arriba, los vuelve a recorrer para conectarlos y con ellos recorrer las subconecciones
            if newOrigin == origin:
                continue
            else:
                try:
                    baseCon = uberMap[newOrigin][origin] #Intenta acceder a la una conexion posible entre 2 vertices A y B, de no existir, dispara except -P
                    nextNode = baseCon.NearNodeInWay #Guarda el nodo mas cercao de la conexion si es que existiese
                    if nextNode == None:
                        nextNode = origin #de no existir, quiere decir que es un arista directa entre 2 vertices, por lo que el "proximo nodo" va a ser el nodo B
                    #Si llega a este punto del codigo, quiere decir que existe una conexion entre A y B
                    for newDest in uberMap[origin]: # por lo que recorro el dict de B para acceder a sus aristas y poder crear las mismas en el diccionario del vertice B
                        newDistance = baseCon.Distance + uberMap[origin][newDest].Distance #la distancia base que va a tener la nueva conexion va a ser, la distancia entre A y B y la distancia entre B y cada nodo X en su DICT
                        try:
                            existingCon = uberMap[newOrigin][newDest] #Intento acceder a una conexion previa entre el nodo A y X, de no existir, voy a exec
                            if existingCon.Distance > newDistance:
                                uberMap[newOrigin][newDest].NearNodeInWay = nextNode
                                uberMap[newOrigin][newDest].Distance = newDistance
                        except:
                            linkedAddress = domain.Distance() #Creo una nueva conexion con los datos encontrados anteriormente
                            linkedAddress.Distance = newDistance 
                            linkedAddress.NearNodeInWay = nextNode
                            uberMap[newOrigin][newDest] = linkedAddress  #Ahora existe una nueva conexion (directa o no) entre A y X con distancia "newDistance" y "nextNode" de proximo nodo
                except:
                    continue