# nome = input("Digite seu Nome: ")
# print ("Olá,",nome)

# nome = input("Digite seu Nome: ")
# idade = int(input("Digite sua Idade: "))
# print ("Olá,",nome,"você tem",idade,"anos de idade")

# nome = input("Digite o seu Nome: ")
# print ("Olá,",nome)
# altura = float(input("Qual sua altura? "))
# print ("Você tem",altura,"de altura")
# print ("Muito Obrigado por usar nosso aplicativo")

# enderecoRua = input("Olá, usuário! Em qual rua você mora? ")
# enderecoNumero = int(input("Qual o número da sua casa? "))
# enderecoBairro = input("Em qual bairro você mora? ")
# enderecoCidade = input("Em qual cidade? ")
# enderecoCEP = input("Qual o CEP de onde você mora? ")
# print ("O usuário mora na Rua",enderecoRua, "número",enderecoNumero, "bairro",enderecoBairro, "na cidade de",enderecoCidade, "com CEP",enderecoCEP)

# valor1 = int(input("Digite um número inteiro: "))
# valor2 = int(input("Digite mais um número inteiro: "))
# valor3 = int(input("Digite outro número inteiro: "))
# valor4 = int(input("Digite mais outro número inteiro: "))
# valor5 = int(input("Digite um último número inteiro: "))
# soma = valor1 + valor2 + valor3 + valor4 + valor5
# produto = valor1*valor2*valor3*valor4*valor5
# print ("A soma de todos os valores é igual a:",soma)
# print ("O produto de todos os valores é igual a:",produto)

# A = int(input("Digite o valor de A: "))
# B = int(input("Digite o valor de B: "))
# C = int(input("Digite o valor de C: "))
# D = int(input("Digite o valor de D: "))
# E = int(input("Digite o valor de E: "))
# areaTriangulo = (B * C) / 2
# perimetroRetangulo = A+B+C+D
# areaCirculo = 3.14 * (E * E)
# print ("A área do triangulo é igual a:",areaTriangulo)
# print ("O perímetro do retângulo é igual a:",perimetroRetangulo)
# print ("A área do circulo é igual a:",areaCirculo)

# nota1 = float(input("Digite sua nota do trabalho: "))
# nota2 = float(input("Digite aqui sua nota da prova: "))
# nota3 = float(input("Digite sua nota do teste: "))
# notafinal = (nota1*0.1)+(nota2*0.6)+(nota3*0.3)
# print ("Sua nota final é igual a:",notafinal)

atividadePratica = float(input("Digite aqui a sua nota na Atividade Prática: "))
atividadeTeorica = float(input("Digite aqui a sua nota na Atividade Teórica: "))

provaEmLaboratorio = float(input("Digite aqui a sua nota na Prova Em Laboratório: "))
testeTeorico = float(input("Digite aqui a sua nota no Teste Teórico: "))
trabalhoExtraclasse = float(input("Digite aqui a sua nota no Trabalho Extraclasse: "))

grauA = ((atividadePratica*0.45)+(atividadeTeorica*0.55))*0.33
grauB = ((provaEmLaboratorio*0.6)+(testeTeorico*0.2)+(trabalhoExtraclasse*0.2))*0.67
notafinal = grauA+grauB

print ("Sua nota final é igual a:",notafinal)