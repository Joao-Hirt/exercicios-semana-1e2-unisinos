a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

xPositivo = ((b * -1) + (b**2 - 4 * a * c) ** (1/2)) / (2 * a)
xNegativo = ((b * -1) - (b**2 - 4 * a * c) ** (1/2)) / (2 * a)

print ("---------- Raíses da equação: ----------")
print ("x Positivo =",xPositivo)
print ("x Negativo =",xNegativo)