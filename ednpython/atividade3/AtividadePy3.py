# ---------------------- 1 - Área da Circunferência ----------------------
pi = 3.14159265
raio = float(input("Digite o raio da circunferência: "))
area = pi * (raio ** 2)
print(f"A={area:.4f}\n")

# ---------------------- 2 - Classificador de Idade ----------------------
idade = int(input("Digite sua idade: "))

if 0 <= idade <= 12:
    print("Criança\n")
elif 13 <= idade <= 17:
    print("Adolescente\n")
elif 18 <= idade <= 59:
    print("Adulto\n")
elif idade >= 60:
    print("Idoso\n")
else:
    print("Idade inválida\n")

# ---------------------- 3 - Calculadora de IMC ----------------------
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}\n")

# ---------------------- 4 - Conversor de Temperatura ----------------------
temperatura = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C/F/K): ").upper()
destino = input("Digite a unidade de destino (C/F/K): ").upper()

resultado = None

if origem == "C":
    if destino == "F":
        resultado = (temperatura * 9/5) + 32
    elif destino == "K":
        resultado = temperatura + 273.15
    else:
        resultado = temperatura

elif origem == "F":
    if destino == "C":
        resultado = (temperatura - 32) * 5/9
    elif destino == "K":
        resultado = (temperatura - 32) * 5/9 + 273.15
    else:
        resultado = temperatura

elif origem == "K":
    if destino == "C":
        resultado = temperatura - 273.15
    elif destino == "F":
        resultado = (temperatura - 273.15) * 9/5 + 32
    else:
        resultado = temperatura

else:
    print("Unidade de origem inválida")

if resultado is not None:
    print(f"Temperatura convertida: {resultado:.2f} {destino}\n")

# ---------------------- 5 - Verificador de Ano Bissexto ----------------------
ano = int(input("Digite o ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Ano bissexto\n")
else:
    print("Não é bissexto\n")

# ---------------------- 6 - Calculadora de Comissão ----------------------
nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: "))
total_vendas = float(input("Digite o total de vendas: "))

comissao = total_vendas * 0.15
total_receber = salario_fixo + comissao

print(f"TOTAL = R$ {total_receber:.2f}\n")

# ---------------------- 7 - Calculadora da Média ----------------------
N1, N2, N3, N4 = map(float, input("Digite as quatro notas separadas por espaço: ").split())

media = (N1*2 + N2*3 + N3*4 + N4*1) / 10
print(f"Media: {media:.1f}")

if media >= 7.0:
    print("Aluno aprovado.\n")
elif media < 5.0:
    print("Aluno reprovado.\n")
else:
    print("Aluno em exame.")
    nota_exame = float(input("Digite a nota do exame: "))
    print(f"Nota do exame: {nota_exame:.1f}")
    media_final = (media + nota_exame) / 2
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media_final:.1f}\n")

