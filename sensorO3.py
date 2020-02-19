import serial
import random
from time import sleep

port = "COM9"
ser = serial.Serial(port,9600)
ser.flushInput()
ser.flushOutput()
while True:
    #concentracion de OZONO(O3) 
    O3=random.uniform(0.0,0.60)
    n1 = str(O3)
    n1 += "\r\n"
    ser.write(n1.encode())
    print ("enviando concentracion de O3 es:",O3)
    
    #concentracion de DIOXIDO DE AZUFRE(SO2) 
    SO2=random.uniform(0.0,1.00)
    n2 = str(SO2)
    n2 += "\r\n"
    ser.write(n2.encode())
    print ("enviando concentracion de SO2 es:",SO2)
    
    #concentracion de DIOXIDO DE NITROGENO(NO2) 
    NO2=random.uniform(0.0,2.00)
    n3 = str(NO2)
    n3 += "\r\n"
    ser.write(n3.encode())
    print ("enviando concentracion de NO2 es:",NO2)
    
    #concentracion de MONOXIDO DE CARBONO(CO) 
    CO=random.uniform(0.0,50)
    n4 = str(CO)
    n4 += "\r\n"
    ser.write(n4.encode())
    print ("enviando concentracion de CO es:",CO)
    
    #concentracion de FRACCION RESPIRABLE DE PARTICULAS SUSPENDIDAS TOTALES(PM10) 
    PM10=random.uniform(0.0,600)
    n5 = str(PM10)
    n5 += "\r\n"
    ser.write(n5.encode())
    print ("enviando concentracion de PM10 es:",PM10)
    print("--------------------------------------------")
    
    
    sleep(10)
ser.close()
