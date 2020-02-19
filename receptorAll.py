from flask import Flask, jsonify, request, render_template
import serial
port = "COM10"
ser = serial.Serial(port,9600)
while True:
	IMECA=0.0
	CalidadAire = ""
	IMECARRAY=[]
	
	#CALCULOS EN RANGO 2 DE https://www.redalyc.org/pdf/944/94403111.pdf
	#hola desde GIT
	#Recibe O3
	O3 = ser.readline().decode()
	O3 = O3.replace("\r\n","")
	O3 = float(O3)
	IMECAO3 = (816.3265*O3)+10.204
	IMECARRAY.append(IMECAO3)
	
	#Recibe SO2
	SO2 = ser.readline().decode()
	SO2 = SO2.replace("\r\n","")
	SO2 = float(SO2)
	IMECASO2 = (459.77*SO2)+40.2298
	IMECARRAY.append(IMECASO2)
	
	#Recibe NO2
	NO2 = ser.readline().decode()
	NO2 = NO2.replace("\r\n","")
	NO2 = float(NO2)
	IMECANO2 = (223.4637*NO2)+53.0726
	IMECARRAY.append(IMECANO2)
	
	#Recibe CO
	CO = ser.readline().decode()
	CO = CO.replace("\r\n","")
	CO = float(CO)
	IMECACO = (10.2564*CO)-12.82
	IMECARRAY.append(IMECACO)
	
	#Recibe PM10
	PM10 = ser.readline().decode()
	PM10 = PM10.replace("\r\n","")
	PM10 = float(PM10)
	IMECAPM10 = (0.3333*PM10)+83.33
	IMECARRAY.append(IMECAPM10)
	
	for elem in IMECARRAY:
		if (elem > IMECA):
			IMECA=elem
	
	
	if(IMECA > 0 and IMECA < 101):
		CalidadAire = "Satisfactorio"
	elif(IMECA > 100 and IMECA <201):
		CalidadAire = "No Satisfactorio"
	elif(IMECA > 200 and IMECA <301):
		CalidadAire = "Mala"
	elif(IMECA > 300 and IMECA <501):
		CalidadAire = "Muy Mala"

	print("recibiendo concentracion de O3:",O3)
	print("recibiendo concentracion de SO2:",SO2)
	print("recibiendo concentracion de NO2:",NO2)
	print("recibiendo concentracion de CO:",CO)
	print("recibiendo concentracion de PM10:",PM10)
	print("IMECAO3 es : ",IMECA)
	print("Calidad del Aire:",CalidadAire)
	print("--------------------------------------------")
ser.close()
