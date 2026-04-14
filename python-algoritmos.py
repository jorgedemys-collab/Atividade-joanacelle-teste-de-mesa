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

# 11. Par positivo / par negativo / caso contrário
a = int(input("Digite um número: "))
if a % 2 == 0 and a > 0:
    print("Par positivo")
elif a % 2 == 0 and a < 0:
    print("Par negativo")
else:
    print("Ímpar")

# 12. Maiúscula ou minúscula
letra = input("Digite uma letra: ")
if letra.isupper():
    print("Maiúscula")
else:
    print("Minúscula")

# 13. Maior que 100 ou dobro
a = int(input("Digite um número: "))
if a > 100:
    print(a / 2)
else:
    print(a * 2)

# 14. Múltiplo de 3
a = float(input("Digite um número: "))
b = int(a)
if b % 3 == 0:
    print("Múltiplo de 3")
else:
    print("Não é múltiplo de 3")

# 15. Intervalo 10 a 20
a = int(input("Digite um número: "))
if a >= 10 and a <= 20:
    print("Dentro")
else:
    print("Fora")

# 16. Tipo de número
a = int(input("Digite um número: "))
if a == 0:
    print("Zero")
elif a > 0:
    print("Positivo")
else:
    print("Negativo")

# 17. Classificação de idade
idade = int(input("Digite a idade: "))
if idade < 18:
    print("Menor de idade")
elif idade <= 59:
    print("Adulto")
else:
    print("Idoso")

# 18. Classificação completa
a = int(input("Digite um número: "))
if a == 0:
    print("Zero")
elif a > 0 and a % 2 == 0:
    print("Par positivo")
elif a > 0 and a % 2 != 0:
    print("Ímpar positivo")
elif a < 0 and a % 2 == 0:
    print("Par negativo")
else:
    print("Ímpar negativo")

# 19. Iguais ou diferença
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
if a == b:
    print("Iguais")
else:
    print(a - b)

# 20. Intervalo 0 a 100
a = int(input("Digite um número: "))
if a >= 0 and a <= 100:
    print("Dentro do intervalo")
else:
    print(a)
