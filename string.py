nome = "matheus Piccoli"
nome2 = "MatheusPiccoli"

print(nome.split(" ")) # ['Matheus', 'Piccoli']
print(nome2[1]) # a
print(nome[1:7]) # slice -> "atheus"
print(nome.lower())
print(nome.upper())
print(nome.title()) # Deixa em maiusculo a primeira letra e a primeira letra depois do espaço

print(nome[::2])
print(nome.startswith("m"))
print(nome.startswith("M"))