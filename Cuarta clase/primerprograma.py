#Calculadora que reciba numeros pero que no reciba lo que sea.
#Tenga todos los tipos de errores
#Tenga suma, resta, multiplicación, división, exponenciación
#Operacion que rciba 2 numeros y la operacion que va a realizar

def calculadora (x, y, op):
    print("Bienvenido a la calculadora de Yesi")    
    try:
        num1= float(x)
        num2= float(y)
        
        if op == "+":
            return num1 + num2
        elif op == "-":
            return num1 - num2
        elif op == "*":
            return num1 * num2
        elif op == "/":
            if num2 == 0:
                return "Error: División por cero no permitida."
            return num1 / num2
        elif op == "**":
            return num1 ** num2
        else:
            return "Error: Operación no válida."
    except ValueError:
        return "Error: Entrada no válida. Por favor ingresa números."

x= input ("Ingresa el primer numero ")
y= input ("Ingresa el segundo numero ")
op= input("Ingresa la operación a realizar (suma (+), resta (-), multiplicación (*), división (/), exponenciación (**)) ")

resultado= calculadora (x, y, op)
print("El resultado es: ", resultado)
