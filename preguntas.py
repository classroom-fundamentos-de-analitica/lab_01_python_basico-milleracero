"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    acum = 0
    with open("data.csv") as f:
        for line in f:
            line = line.split()
            acum+=int(line[1])
    
    return acum



def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    cuenta ={}
    with open("data.csv") as f:
        for line in f:
            line = line.split()
            if line[0] in cuenta:
                cuenta[line[0]]+=1
            else:
                cuenta[line[0]]=1
    return (sorted(cuenta.items()))


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """

    cuenta ={}  
    with open("data.csv") as f:
        for line in f:
            line = line.split()
            if line[0] in cuenta:
                cuenta[line[0]]+=int(line[1])
            else:
                cuenta[line[0]]=int(line[1])          
    return (sorted(cuenta.items()))


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """

    cuenta ={}  
    with open("data.csv") as f:
        for line in f:
            line = line.split()
            mes = line[2].split("-")[1]
            if mes in cuenta:
                cuenta[mes]+=1
            else:
                cuenta[mes]=1
    return(sorted(cuenta.items()))
   

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    cuenta ={}  
    with open("data.csv") as f:
        for line in f:
            line = line.split()

            if line[0] in cuenta:
                if int(line[1]) > int(cuenta[line[0]][0]):
                    cuenta[line[0]][0]=int(line[1])

                elif int(line[1]) < int(cuenta[line[0]][1]):
                    cuenta[line[0]][1]=int(line[1]) 

            else:
                cuenta[line[0]]=[int(line[1]),int(line[1])]
    result = sorted(cuenta.items())
    max_min = []
    for i in result:
        max_min.append((i[0],i[1][0],i[1][1]))
    return max_min



def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """

    cuentas = {}    

    with open("data.csv") as f:
        for line in f:
            line = line.split()
            dic = line[4].split(",")
            for i in dic:
                clave = i.split(":")[0]
                
                valor = int(i.split(":")[1])

                if clave in cuentas:
                    if valor > cuentas[clave][0]:
                        cuentas[clave][0] = valor
                    elif valor < cuentas[clave][1]:
                        cuentas[clave][1] = valor
                else:
                    cuentas[clave] = [valor,valor]
    result = sorted(cuentas.items())    
    max_min = []
    for i in result:
        max_min.append((i[0],i[1][1],i[1][0]))

    return max_min

    


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

    cuenta ={}
    with open("data.csv") as f:
        for line in f:
            line = line.split()
            if line[1] in cuenta:
                cuenta[line[1]].append(line[0])
            else:
                cuenta[line[1]]=[line[0]]
    return sorted(cuenta.items())


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    cuenta ={}
    with open("data.csv") as f:
        for line in f:
            line = line.split()
            if line[1] in cuenta:
                if line[0] not in cuenta[line[1]]:
                    cuenta[line[1]].add(line[0])
            else:
                cuenta[line[1]]={line[0]}
    

    result = []
    for i in sorted(cuenta.items()):
        result.append((int(i[0]),sorted(list(i[1]))))
    return result
 


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    cuenta ={}  
    with open("data.csv") as f: 
        for line in f:
            line = line.split()
            dic = line[4].split(",")
            for i in dic:
                clave = i.split(":")[0]
                if clave in cuenta:
                    cuenta[clave]+=1
                else:
                    cuenta[clave]=1
    result = dict(sorted(cuenta.items()))   
   
    return result


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """

    total = []
    with open("data.csv") as f:
        for line in f:
            line = line.split()
            gg = line[3].split(",") 
            dic = line[4].split(",")            
            total.append((line[0],len(gg),len(dic)))

    return total


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    cuenta ={}  
    with open("data.csv") as f:
        for line in f:
            line = line.split()
            dic = line[3].split(",")
            for i in dic:
                if i in cuenta:
                    cuenta[i]+=int(line[1])
                else:
                    cuenta[i]=int(line[1])
    result = dict(sorted(cuenta.items()))
    return result
 
def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    cuenta ={}
    with open("data.csv") as f:
        for line in f:
            line = line.split()
            clave = (line[0]) 
            dic = line[4].split(",")
            for i in dic:
                
                valor = int(i.split(":")[1])
                if clave in cuenta:
                    cuenta[clave]+=valor
                else:
                    cuenta[clave]=valor

    result = dict(sorted(cuenta.items()))
    
    return result
 