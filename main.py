users = [
    "Matheus",  # admin user
    "Matheus123!",  # admin password
    "Pedro",  # member user
    "Pedro123!"  # member password
]

print("   Olá, preencha com suas informações para continuar!")
print("")
print("")
user = input("   Usuario: ")
password = input("   Senha: ")

try:
    if not users[users.index(user)] is None:
        index = users.index(user)
        if users[index + 1] == password:
            print("Seja muito bem-vindo, " + user + "!")
except:
    print("Usuario nao identificado")
