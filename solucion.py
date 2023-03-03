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
print(diccionario_sumaValoresCol5xletraCol1)
                




