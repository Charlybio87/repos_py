#Funcion input()
print("Dime lo que sea...")
anything = input()
print("Hmm...", anything, "... ¿en serio?")
#con Argumento
anything = input("Dime lo que sea...")
print("Hmm...", anything, "...¿en serio?")
#Conversio de tipos
anything = float(input("Ingresa un número: "))
something = anything ** 2.0
print(anything, "a la potencia de 2 es", something)
#
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es:", (leg_a**2 + leg_b**2) ** .5)
#Operadores de cadena
fnam = input("¿Me puedes dar tu nombre por favor? ")
lnam = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + fnam + " " + lnam + ".")
#
print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")
#Conversiones otros tipos
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es " + str((leg_a**2 + leg_b**2) ** .5))
#Laboratorio in out
a = float(input("Ingresa el primer valor: "))
b = float(input("Ingresa el segundo valor: "))
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("\n¡Eso es todo, amigos!")
#Laboratorio Operadores y expresiones
x = float(input("Ingrese un valor de x: "))
y = 1./(x + 1./(x + 1./( x + 1./x)))
print("El valor de y es ",y)
