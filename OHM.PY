#Este programa calcula la ley de Ohm
print("Ley de Ohm")
print("selecciona la opcion")
opcion=int(input("1=Voltaje, 2=Corriente, 3=Resistencia:"))
try:
    if opcion==1:
        resistencia=float(input("ingresa la resistencia(Ohm):"))
        corriente=float(input("ingresa la corriente(amperios):"))
        voltaje=resistencia*corriente
        print("el voltaje es:",voltaje,"voltios")
    elif opcion==2:
         voltaje=float(input("ingresa el voltaje (voltios):"))
         resistencia=float(input("ingrear la resistencia(ohm):"))
         corriente=voltaje/resistencia
         print("la corriente es:",corriente,"amperios")
    elif opcion==3:
        voltaje=float(input("ingresa el voltaje (voltios):"))
        corriente=float(input("ingresa la corriente(amperios):"))
        resistencia=voltaje/corriente
        print("La resistencia es:",resistencia,"Ohm")
    else:
        print("opcion no valida")
except ValueError:             
    print("Error: Entrada no valida. Por favor, ingresa un numero.")