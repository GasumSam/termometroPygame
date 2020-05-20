strTipo = input("Temperatura de entrada en Fahrenheit o Celsius (F/C)")
strTemp = input("Valor de la temperatura: ")

temp = float(strTemp)

if strTipo == 'c' or strTipo == 'C':
    strIN = 'C'
    strOUT = 'F'
    output = (temp *  9/5) + 32
else:
    strIN = 'F'
    strOUT = 'C'
    output = (temp - 32) * 5/9
    
print("\n{}º{} son {}º{}".format(temp, strIN, output, strOUT))