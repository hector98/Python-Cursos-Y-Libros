import os
import datetime

users = []
ids = []

def validates(field, len_min, len_max, name_field):
    if len(field) >= len_min and len(field) <= len_max:
        return field
    else:
        print(f"El {name_field} debe tener entre {len_min} y {len_max} caracteres")
        field = input(f"Ingresa su {name_field}: ")
        return validates(field, len_min, len_max, name_field)
    

def register(num_user, ids):
    print(f"Ingresa los datos del Usuario {num_user}")
    name = validates(input("Ingresa su nombre: "), 5, 50, "nombre")
    last_name = validates(input(f"Ingresa su apellido: "), 5, 50, "apellido")
    number_phone = validates(input("Ingresa su numero de telefono: "), 10, 10, "numero de telefono")
    email = validates(input("Ingresa su correo: "), 5, 50, "email")

    user = {
        "id": ids,
        "name": name,
        "last_name": last_name,
        "number_phone": number_phone,
        "email": email
        }
    return user

def idsAdd(num_user):
    date = datetime.datetime.now()
    ids = num_user * (date.year + date.month + date.day + date.hour + date.minute + date.second + date.microsecond)
    id_hex = ""
    while ids > 0:
        aux = ids % 16

        if aux == 10:
            id_hex += "A"
        elif aux == 11:
            id_hex += "B"
        elif aux == 12:
            id_hex += "C"
        elif aux == 13:
            id_hex += "D"
        elif aux == 14:
            id_hex += "E"
        elif aux == 15:
            id_hex += "F"
        else:
            id_hex += str(aux)

        ids = ids // 16

    return id_hex[::-1]


def findUserById(id_u):
    find = False
    find_user = ""
    for user in users:
        if user["id"] == id_u:
            find = True
            find_user = user
            break
    return [find, find_user]


def editUser(id_user):
    print(f"Ingresa los datos del usuario {id_user}")
    name = validates(input("Ingresa su nombre: "), 5, 50, "nombre")
    last_name = validates(input(f"Ingresa su apellido: "), 5, 50, "apellido")
    number_phone = validates(input("Ingresa su numero de telefono: "), 10, 10, "numero de telefono")
    email = validates(input("Ingresa su correo: "), 5, 50, "email")

    edit_user = {
        "id": id_user,
        "name": name,
        "last_name": last_name,
        "number_phone": number_phone,
        "email": email
        }
    return edit_user


def deleteUser(user):
    users.remove(user)
    #ids.remove(user["id"])


def showUser(id):
    find, user = findUserById(id)

    if find:
        print(f"\nLos datos del usuario son:\nId: {user['id']}\nName: {user['name']}\nLast Name: {user['last_name']}\nNumber Phone: {user['number_phone']}\nEmail: {user['email']}")
        print("Deseas editar o eliminar el usuario? \n(0)Nada \n(1)Editar \n(2)Eliminar")
        option = int(input("Ingresa tu opcion: "))

        if option == 1:
            users[users.index(user)] = editUser(user["id"])
            print("El usuario ha sido editado con exito")
        elif option == 2:
            deleteUser(user)
            print("El usuario ha sido eliminado con exito")
    else:
        print("No se encontro el usuario")

    menu()


def menu():
    global users, ids
    #os.system("clear")
    print("Menu: \n(1)Deseas registrar nuevos usuarios? \n(2)Deseas listar todos los usuarios? \n(3)Deseas mostrar los datos de un usuario por su id?")
    option = int(input("Ingresa tu opcion: "))
    
    if option == 1:
        n = int(input("Cuantos usuarios deseas registrar: "))
        for i in range(n):
            ids.append(idsAdd(i+1))
            users.append(register(i+1, idsAdd(i+1)))
            print(f"El Usuario {i+1} ha sido registrado con exito con el id {users[-1]['id']}!!!!!")
            print(f"En breve recibira un correo a {users[-1]['email']}\n")
    elif option == 2:
        for user in users:
            print(f"Id: {user['id']} Name: {user['name']}")
    elif option == 3:
        id = input("Ingresa el id del usuario: ")
        showUser(id)
    else:
        print("Ingresa una opcion valida")
        return menu(users, ids)

    print("Deseas volver al menu?")
    continue_ = input("Ingresa 'S' o 'N': ")
    return menu() if continue_.upper() == "S" else exit


def main():
    menu()
    print("Gracias por usar el programa")

    """
    Mostrar los datos de todos los usuarios registrados
    i = 1
    for user in  users:
        print(f"Los datos del usuario {i} son: ")
        for key, value in user.items():
            print(f"{key}: {value}")
        print("\n")
        i += 1
    """


if __name__ == "__main__":
    main()
