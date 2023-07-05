# import random
#
# num = int(input('Quantos números aleatórios você deseja gerar? '))
#
# for i in range(num):
#     print(random.randint(1,60))

# import random
#
# # gerando uma lista de 6 números aleatórios no intervalo de 1 a 60 sem repetições
# numeros = random.sample(range(1, 61), 6)
#
# # ordenando a lista em ordem crescente
# numeros.sort()
#
#     # imprimindo os números na tela
# print("Números sorteados:")
# for num in numeros:
#     print(num)

### PROJETO DE 'SURPRESINHA' DE LOTERIA

# Importação da biblioteca de números aleatórios
import random

# pedindo ao usuário o número de elementos que deseja gerar
n = int(input("Digite o número de elementos que deseja gerar (entre 6 e 15): "))

# verificando se o número digitado pelo usuário está dentro do intervalo permitido
while n < 6 or n > 15:
    print("Número inválido. O número de elementos deve estar entre 6 e 15.")
    n = int(input("Digite o número de elementos que deseja gerar (entre 6 e 15): "))

# gerando uma lista de n números aleatórios sem repetições no intervalo de 1 a 60
numeros = random.sample(range(1, 61), n)

# ordenando a lista em ordem crescente
numeros.sort()

# imprimindo os números na tela
print("Números sorteados:")
for num in numeros:
    print(num)
