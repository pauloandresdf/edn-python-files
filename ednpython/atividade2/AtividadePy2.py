#Conversor de moedas.
# Valores das moedas
valor_em_reais = 100.00
taxa_dolar = 5.70
taxa_euro = 6.40
# Conversões
valor_em_dolares = valor_em_reais / taxa_dolar
valor_em_euros = valor_em_reais / taxa_euro
# Exibição dos resultados
print(f"Valor em Reais: R$ {valor_em_reais: .2f}")
print("Valor em Dólares: $", round(valor_em_dolares, 2))
print("Valor em Euros: €", round(valor_em_euros, 2))


# Calculadora de desconto
# Informações do produto
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20
# Cálculo do desconto
valor_desconto = preco_original * (porcentagem_desconto / 100)
preco_final = preco_original - valor_desconto
# Exibição dos resultados
print ("Produto:", nome_produto)
print(f"Preço Original: R$ {preco_original: .2f}")
print("Desconto:", porcentagem_desconto, "%")
print(f"Valor de desconto: R$ {valor_desconto: .2f}")
print(f"Preço final: R$ {preco_final: 2f}")

# Calculadora de Média Escolar
# Notas do estudante
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5
# Cálculo da média
media = (nota1 + nota2 + nota3) / 3
print(f"Media: {media: 2f}")

# Calculadora de Consumo de Combustível
# Dados da viagem
distancia_percorrida = 300 # em quilômetros (km)
combustivel_gasto = 25 # em litros (1)
# Cálculo do consumo médio
consumo_medio = distancia_percorrida / combustivel_gasto
# Exibição do resultado print ("Dados da viagem:")
print(f"Distância percorrida: {distancia_percorrida} quilômetros (km)")
print(f"Combustível gasto: {combustivel_gasto} litros (1)")
print ("Consumo médio: ", round (consumo_medio, 2), "km/1")

#Calculadora de salário por horas trabalhadas
# Ler os valores informados pelo usuário
numero_funcionario = int(input("Insira o número do funcionário: "))
horas_trabalhadas = int(input("Insira a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Insira o valor da hora trabalhada: "))
# Cálculo do salário
salario = horas_trabalhadas * valor_por_hora
# Exibir o resultado para o usuário
print ("Número do funcionário: ", numero_funcionario)
print ("Salário = R$", round(salario,2))
