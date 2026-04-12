Atividade-joanacelle-teste-de-mesa

# 1. Positivo ou negativo
a = int(input("Digite um número: "))
if a >= 0:
    print("positivo")
else:
    print("negativo")

# 2. Dobro do valor
a = int(input("Digite um número: "))
print(a * 2)

# 3. Tipo da variável
a = int(input("Digite um número: "))
print(type(a))

# 4. Par ou ímpar
a = int(input("Digite um número: "))
if a % 2 == 0:
    print("par")
else:
    print("ímpar")

# 5. Converter para inteiro
a = float(input("Digite um número: "))
print(int(a))

# 6. Maior entre dois números
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
if a > b:
    print(a)
else:
    print(b)

# 7. Maior que 10 ou não
a = int(input("Digite um número: "))
if a > 10:
    print("Maior que 10")
else:
    print("Menor ou igual a 10")

# 8. Raiz ou inválido
a = int(input("Digite um número: "))
if a > 0:
    print(a ** 0.5)
else:
    print("Número inválido")

# 9. Float e metade
a = int(input("Digite um número: "))
b = float(a)
print(b)
print(b / 2)

# 10. Intervalo 0 a 10
a = int(input("Digite um número: "))
if a >= 0 and a <= 10:
    print("Dentro do intervalo")
else:
    print("Fora do intervalo")
