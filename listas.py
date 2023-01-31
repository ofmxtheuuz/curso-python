lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista2 = [ "a", "b", "c", "d", "e", "f", "g"]
lista3 = list(range(11))
lista4 = lista1 + lista2 + lista3

print(lista4)

lista1.extend([2, 3, 4])
lista1.append(1)

print(lista1)

if "a" in lista2:
    print("encontrei o A")

if "1" in lista1:
    print("encontrei o 1 string")
else:
    print("nao encontrei o 1 string")

print(type(str(lista1[1])))

print(list("Ola"
           ""))