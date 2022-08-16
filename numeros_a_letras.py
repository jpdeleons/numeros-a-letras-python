stUnidades = ["CERO","UNO","DOS","TRES","CUATRO","CINCO","SEIS","SIETE","OCHO","NUEVE","DIEZ","ONCE","DOCE","TRECE","CATORCE","QUINCE"]
stDecenas = ["","DIEZ","VEINTE","TREINTA","CUARENTA","CINCUENTA","SESENTA","SETENTA","OCHENTA","NOVENTA"]
stCentenas = ["","CIEN","DOSCIENTOS","TRESCIENTOS","CUATROCIENTOS","QUINIENTOS","SEISCIENTOS","SETECIENTOS","OCHOCIENTOS","NOVECIENTOS"]

nun = int(input("Dime un numero: "))
if nun < 0 or nun > 999:
    print ("Error en el numero")
else:
    unidades = nun % 10
    decimales = nun % 100
    decenas = (nun // 10) % 10 
    centenas = nun // 100

    if centenas != 0:
        if centenas == 1:
            if decimales == 0:
                print ("CIEN", end="")
            else:
                print ("CIENTO", end="")
        else:
            print (stCentenas[centenas], end="")
        if decimales != 0:
            print (" ", end="")

    if decimales <= 15:
        if decimales != 0 or centenas == 0:
            print (stUnidades[decimales], end="")
    else:
        if decenas == 1:
            print ("DIECI", end="")
        elif decenas == 2:
            if unidades == 0:
                    print ("VEINTE", end="")
            else:
                    print ("VEINTI", end="")
        else:
                print (stDecenas[decenas])
                if unidades != 0:
                    print (" Y ", end="")
        if unidades != 0:
            print(stUnidades[unidades], end = "")            
    print ("")

            
