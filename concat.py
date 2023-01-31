nome = input("Qual o seu nome ")
idade = input("Qual é a sua idade ")
sexo = input("Qual é o seu sexo ")

print()

# Exemplo de concatenacao antigo
print("Ola %s" % nome)
print("Seja bem-vindo %s, voce tem %s e é do sexo %s" % (nome, idade, sexo))

print()

# Exemplo de concatenacao novo
print("Concat - Oi {0}, voce tem {1} anos".format(nome, idade))

# Exemplo de concatenacao atual
print(f"Concat 2 - Bom dia {nome}")

print("oi", "oi") # a virgula serve como um espaço

print()

# O input retorna um string
print(type(input("tipo ")))

# vc pode converter
print(type(int(input("tipo "))))
