## CALCULADORA JADA

print ("BIENVENIDO A NUESTRA CALCULADORA DE OPERACIONES BASICAS")

print ("Que operacion desea realizar?")

print("1. Suma")
print("2. Resta")
print("3. multiplicacion")
print("4. division")

operacion= int(input())

if operacion==1:
    print("ingrese el primer numero a sumar")
    num1= float(input())
    print("ingrese el segundo numero a sumar")
    num2= float(input())
    resultado=num1+num2
    print("la suma de los dos numeros ingresados es ", resultado)
elif operacion==2:
    print("ingrese el minuendo o valor del cual se va restar")
    num1 = float(input())
    print("ingrese el sustraendo o valor a restar")
    num2= float(input())
    resultado=num1-num2
    print("el valor de la resta es ", resultado)
elif operacion==3:
    print("ingrese el primer numero a multiplicar")
    num1 = float(input())
    print("ingrese el segundo numero a multiplicar")
    num2 = float(input())
    resultado=num1*num2
    print("el valor de la multiplicacion es ", resultado)
elif operacion==4:
    print("ingrese el numero que quiere dividir")
    num1 = float(input())
    print("ingrese en cuanto quiere dividirlo")
    num2 = float(input())

    if num2==0:
        print("usted esta dividiendo entre cero lo cuales una indeterminacion error")
    else:
        resultado = num1 / num2
        print("el valor de la division es ", resultado)

else:
    print("usted a seleccionado una operacion que no esxite")


print ("GRACIAS POR UTILIZAR NUESTRA CALCULADORA")
