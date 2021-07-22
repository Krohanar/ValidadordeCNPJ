from regex import split as sp


def retornar_string(variavel, variavel2):
    for valor in range(len(variavel)):
        variavel2 = variavel2 + variavel[valor]
    variavel2 = [x for x in variavel2]
    for valor in range(len(variavel2)):
        variavel2[valor] = int(variavel2[valor])
    return variavel2


def tupla_cnpj(cnpj, calculadora):
    cnpj1 = zip(cnpj, calculadora)
    calculadora = [x * y for x, y in cnpj1]
    soma = 0
    for valor in range(len(calculadora)):
        soma = calculadora[valor] + soma
    return soma


cnpjinic = input("Digite aqui seu CNPJ")
cnpj1 = sp("[./-]", cnpjinic)
cnpj200 = sp("[./-]", cnpjinic)
cnpj1.pop(-1)

cnpj2 = ""
cnpj2 = retornar_string(cnpj1, cnpj2)
# cnpj2 juntou

calculador1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

calculo = tupla_cnpj(cnpj2, calculador1)

primeiro_digito = (11 - (calculo % 11))

# agora o segundo digito
if (primeiro_digito <= 9):
    cnpj1.append(str(primeiro_digito))
else:
    cnpj1.append(str(0))

cnpj_calculo = ""
cnpj_calculo = retornar_string(cnpj1, cnpj_calculo)

calculador2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
calculo2 = tupla_cnpj(cnpj_calculo, calculador2)

segundo_digito = (11 - (calculo2 % 11))

if (segundo_digito <= 9):
    cnpj1.append(str(segundo_digito))
else:
    cnpj1.append(str(0))

final = ""
for valor in range(len(cnpj1)):
    final += cnpj1[valor]

inicial = ""
for valor in range(len(cnpj200)):
    inicial += cnpj200[valor]

if (inicial == final):
    print('Validado')
else:
    print('CPNJ Invalido')
