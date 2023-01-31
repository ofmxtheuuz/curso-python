list1 = [9, 2, 5, 1, 7,  2, 6, 6, 1, 8, 3, 6, 4]
list1.sort() # ordena a lista
print(list1)

list2 = [ "Pedro", "Arthur", "Matheus" ]
list2.sort() # ordena listas de strings tambem
print(list2)

print(list(range(11)))

print(list1.count(6)) # quantas vezes o 6 aparecem
print(len(list1))

list1.append(["entrei aqui",  5, 5, 5])
print(list1)

list1.extend(["alou", "alou"])
print(list1)

if 9 in list1: # se tem 9 em "list1"
    print("tem")
else:
    print("nao tem")