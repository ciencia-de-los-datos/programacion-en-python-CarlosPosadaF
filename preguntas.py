"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
string_var = """E	1	1999-02-28	b,g,f	jjj:12,bbb:3,ddd:9,ggg:8,hhh:2
A	2	1999-10-28	a,f,c	ccc:2,ddd:0,aaa:3,hhh:9
B	5	1998-05-02	f,e,a,c	ddd:2,ggg:5,ccc:6,jjj:12
A	3	1999-08-28	a,b	hhh:9,iii:5,eee:7,bbb:1
C	6	1999-12-01	f,g,d,a	iii:6,ddd:5,eee:4,jjj:12
A	7	1998-07-28	c,d	bbb:2,hhh:0,ccc:4,fff:1,aaa:7
A	9	1997-02-28	g,d,a	aaa:5,fff:8,ddd:2,iii:0,jjj:7,ccc:1
B	1	1999-05-10	b,a	fff:3,hhh:1,ddd:2
E	2	1997-04-12	d,e,a,f	eee:4,ccc:5,iii:9,fff:7,ggg:6,bbb:2
B	3	1999-11-23	d,b,g,f	bbb:7,jjj:9,fff:5,iii:4,ggg:3,eee:3
C	7	1998-01-17	d,c,f,b	hhh:6,eee:4,iii:0,fff:2,jjj:12
C	5	1998-12-28	d,e,a,c	bbb:7,iii:6,ggg:9
D	3	1999-10-15	g,e,f,b	bbb:9,aaa:3,ccc:6,fff:4,eee:2
E	8	1998-11-01	c,f	aaa:8,ddd:5,jjj:12
B	9	1999-08-12	d,b	ccc:7,jjj:6,fff:7,ddd:3,aaa:2
D	8	1997-12-01	f,e	ccc:8,eee:6,bbb:9,ddd:3
E	3	1997-07-28	e,b,f	bbb:6,iii:3,hhh:5,fff:4,ggg:9,ddd:2
D	5	1998-08-12	g,a	hhh:4,jjj:5,ccc:9
E	8	1999-08-24	e,c,f,a	ccc:1,iii:6,fff:9
E	9	1998-01-23	e,a	bbb:9,aaa:3,fff:1
E	7	1999-06-22	e,f	ddd:9,iii:2,aaa:4
E	3	1999-04-24	c,b,g	ccc:5,fff:8,iii:7
D	5	1999-06-25	c,f,a	eee:3,jjj:17,ddd:7
A	9	1999-08-25	f,a,d	jjj:12,ggg:7,ccc:7,ddd:9,bbb:3
E	4	1997-07-26	c,d	jjj:6,ccc:4,aaa:1,hhh:9,iii:7,ggg:8
E	6	1997-09-24	e,d,c	fff:3,eee:6,iii:4,bbb:7,ddd:4,ccc:1
A	8	1997-09-28	a,e,f	fff:0,ddd:5,ccc:4
E	5	1999-06-22	c,a,g	ggg:6,hhh:3,ddd:9,ccc:10,jjj:7
A	6	1999-07-29	f,e	hhh:6,jjj:13,eee:5,iii:7,ccc:3
C	0	1999-08-22	f,c,a,g	eee:1,fff:4,aaa:2,ccc:7,ggg:10,ddd:6
A	9	1998-04-26	b,f	ccc:6,aaa:9,eee:5,ddd:0,bbb:3
D	3	1998-02-24	b,f	bbb:7,hhh:1,aaa:6,iii:4,fff:9,ddd:5
E	5	1999-03-24	a,c	fff:3,ccc:1,ggg:3,eee:5
B	4	1998-03-23	b,f,c	iii:7,ggg:3,ddd:0,jjj:8,hhh:5,ccc:1
B	6	1999-04-21	f,a,e	hhh:6,ccc:3,jjj:9,bbb:8,ddd:7
D	7	1999-02-29	a,f	aaa:1,fff:5,ddd:3
B	8	1997-05-21	c,a	ddd:5,jjj:17,iii:7,ccc:10,bbb:4
C	9	1997-07-22	c,a,e,f	eee:3,fff:2,hhh:6
E	1	1999-09-28	e,d	fff:9,iii:2,eee:5
E	5	1998-01-26	f,a,d	hhh:8,ggg:3,jjj:5"""

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    # Leer un archivo externo
    #data = open("data.csv", "r").readlines() 

    # Reemplazar el salto de línea
    # list comprenhention
    #data = [linea.replace("\n", " ")for linea in data]
    
    string_vector = string_var.splitlines()
    int_acumulador = 0
    for elemento in string_vector: 
        int_acumulador += int(elemento[2])

    #print(int_acumulador)
    return int_acumulador


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
    string_vector = string_var.splitlines()
    vectorLetras = ["A", "B", "C", "D", "E"]
    listaTuplas = []

    for letra in vectorLetras:
        contLetras = 0
        
        for elemento in string_vector:
            if elemento[0] == letra:
                contLetras += 1

        tupla = (letra, contLetras)
        listaTuplas.append(tupla)

    #print(listaTuplas)
        
    return listaTuplas


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

    string_vector = string_var.splitlines()
    vectorLetras = ["A", "B", "C", "D", "E"]
    listaTuplas = []

    for letra in vectorLetras:
        acumLetra = 0
        for elemento in string_vector:
            if elemento[0] == letra:
                acumLetra += int(elemento[2])

        tupla = (letra, acumLetra)
        listaTuplas.append(tupla)

    #print(listaTuplas)
    return listaTuplas


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

    string_vector = string_var.splitlines()
    vectorMeses = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
    listaTuplas = []

    for mes in vectorMeses:
        contMeses = 0
        acumMeses = 0
            
        for elemento in string_vector:
            string_fechaxlinea = elemento.split("\t")[2].split("-")[1]
                
            if string_fechaxlinea == mes:
                acumMeses += 1

        tupla = ((mes), acumMeses)
        listaTuplas.append(tupla)
            

    #print(listaTuplas)

    return listaTuplas


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

    string_vector = string_var.splitlines()
    vectorLetras = ["A", "B", "C", "D", "E"]
    listaTuplas = []

    for letra in vectorLetras:
        vector = [0, 9]
        for elemento in string_vector:
            if elemento[0] == letra:
                if int(elemento[2]) > int(vector[0]):
                    vector[0] = elemento[2]
                if int(elemento[2]) < int(vector[1]):
                    vector[1] = elemento[2]

                tupla = (elemento[0], int(vector[0]), int(vector[1]))
        listaTuplas.append(tupla)

    #print(listaTuplas)
    
    return listaTuplas


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

    string_vector = string_var.splitlines()
    vectorClaves = ["aaa", "bbb", "ccc", "ddd", "eee", "fff", "ggg", "hhh", "iii", "jjj"]
    listaTuplas = []
    cont = -1
    for clave in vectorClaves:
        vector = [0, 9]
        cont += 1
        for elemento in string_vector:
            string_clavesxlinea = elemento.split("\t")[4].split(",")
                
            for claveValor in string_clavesxlinea:            
                string_clave = claveValor.split(":")
                
                if string_clave[0] == vectorClaves[cont]:
                    if int(string_clave[1]) > int(vector[0]):
                        vector[0] = string_clave[1]
                    if int(string_clave[1]) < int(vector[1]):
                        vector[1] = string_clave[1]

                    tupla = (string_clave[0], int(vector[1]), int(vector[0]))
            
        listaTuplas.append(tupla)
            
    #print(listaTuplas)
    return listaTuplas


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

    string_vector = string_var.splitlines()
    listaTuplas = []
    for i in range(10):
            
        string_letrasxNumero = ""
        for elemento in string_vector:
            string_letraxlinea = elemento.split("\t")
                
            if i == int(string_letraxlinea[1]):
                letra = string_letraxlinea[0]
                string_letrasxNumero += letra
                
                tupla = (i, list(string_letrasxNumero))
            
        listaTuplas.append(tupla)
    #print(listaTuplas) 
    return listaTuplas


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

    string_vector = string_var.splitlines()
    listaTuplas = []
    for i in range(10):
            
        string_letrasxNumero = ""
        for elemento in string_vector:
            string_letraxlinea = elemento.split("\t")
                
            if i == int(string_letraxlinea[1]):
                letra = string_letraxlinea[0]

                if string_letrasxNumero.find(letra) < 0:
                    string_letrasxNumero += letra 
                
                tupla = (i, sorted(string_letrasxNumero))

        listaTuplas.append(tupla)
            
    #print(listaTuplas)  
    return listaTuplas


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

    string_vector = string_var.splitlines()
    vectorClaves = ["aaa", "bbb", "ccc", "ddd", "eee", "fff", "ggg", "hhh", "iii", "jjj"]
    vectorTuplas = [0,0,0,0,0,0,0,0,0,0]
    cont = -1
    for clave in vectorClaves:
        vector = [0, 9]
        cont += 1
        contClaves = 0 
        for elemento in string_vector:
            string_clavesxlinea = elemento.split("\t")[4].split(",")
            
            for claveValor in string_clavesxlinea:            
                string_clave = claveValor.split(":")
                    
                if string_clave[0] == vectorClaves[cont]:
                    
                    contClaves += 1
                    vectorTuplas[cont] = contClaves

    diccionarioClaves = {vectorClaves:vectorTuplas for (vectorClaves,vectorTuplas) in zip(vectorClaves,vectorTuplas)}        
    #print(diccionarioClaves)
    return diccionarioClaves


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

    string_vector = string_var.splitlines()
    listaTuplas = []
    cont = 0

    for elemento in string_vector:
        string_elementosxlinea = elemento.split("\t")
        letra = string_elementosxlinea[0]
        cantLetras = len(string_elementosxlinea[3].split(","))
        cantClaves = len(string_elementosxlinea[4].split(","))

        tupla = (letra, cantLetras, cantClaves)
        listaTuplas.append(tupla)

    #print(listaTuplas)
    return listaTuplas


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

    string_vector = string_var.splitlines()
    vectorClaves = ["a", "b", "c", "d", "e", "f", "g"]
    vectorTuplas = [0,0,0,0,0,0,0]
    cont = -1
    for clave in vectorClaves:
        cont += 1
        acumNumsxletraCol4 = 0
        for elemento in string_vector:
            string_letrasCol4xlinea = elemento.split("\t")[3].split(",")
            int_numCol2 = int(elemento.split("\t")[1])
            
            try:
                indice = string_letrasCol4xlinea.index(clave) > -1
            except:
                continue
            else:
                acumNumsxletraCol4 += int_numCol2
            
        vectorTuplas[cont] = acumNumsxletraCol4

    diccionario_sumaCol2xletraCol4 = {vectorClaves:vectorTuplas for (vectorClaves,vectorTuplas) in zip(vectorClaves,vectorTuplas)}
        
    #print(diccionario_sumaCol2xletraCol4)

    return diccionario_sumaCol2xletraCol4


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

    string_vector = string_var.splitlines()
    vectorLetras = ["A", "B", "C", "D", "E"]
    vectorTuplas = [0,0,0,0,0]
    cont = -1

    for letra in vectorLetras:
        cont += 1
        acumValoresDic = 0
        for elemento in string_vector:
            string_elementosxlinea = elemento.split("\t")
            letraCol1 = string_elementosxlinea[0]

            if letra == letraCol1:
                diccionario = string_elementosxlinea[4].split(",")
                
                for elementoDic in diccionario:
                    acumValoresDic += int(elementoDic.split(":")[1])
                    
        vectorTuplas[cont] = acumValoresDic

    diccionario_sumaValoresCol5xletraCol1 = {vectorLetras:vectorTuplas for (vectorLetras,vectorTuplas) in zip(vectorLetras,vectorTuplas)}

    return diccionario_sumaValoresCol5xletraCol1
