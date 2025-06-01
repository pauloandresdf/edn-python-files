pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro ou 'fim' para encerrar: ")
    if entrada.lower() == "fim":
        break

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
            pares += 1 # a mesma coisa, mas de outra forma. pares = pares + 1
        else:
            print(f"O número {numero} é ímpar.")
            impares += 1
    except ValueError:
        print("Erro encontrado. Por favor, insira um número inteiro.")
        continue

print("\nResultado Final:")
print(f"A quantidade de números pares é: {pares}")
print(f"A quantidade de números ímpares é: {impares}")