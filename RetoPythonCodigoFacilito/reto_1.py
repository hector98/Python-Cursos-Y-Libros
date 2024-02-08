import os
import time
def userNew(name, last_name, email):
    return f"Hola {name} {last_name} en breve recibirás un correo a {email}"


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
    ids = num_user * int(time.clock_gettime(1))
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


def editUser():
    print("Ingresa los datos del usuario")
    name = validates(input("Ingresa su nombre: "), 5, 50, "nombre")
    last_name = validates(input(f"Ingresa su apellido: "), 5, 50, "apellido")
    number_phone = validates(input("Ingresa su numero de telefono: "), 10, 10, "numero de telefono")
    email = validates(input("Ingresa su correo: "), 5, 50, "email")

    edit_user = {
        "name": name,
        "last_name": last_name,
        "number_phone": number_phone,
        "email": email
        }
    return edit_user

def findUserById(users, id_u):
    find = False
    find_user = ""
    for user in users:
        if user["id"] == id_u:
            find = True
            find_user = user
            break
    if find:
        print(f"\nLos datos del usuario son: \nId = {find_user['id']}\nName = {find_user['name']}\nLast Name = {find_user['last_name']}\nNumber Phone = {find_user['number_phone']}\nEmail = {find_user['email']}\n")

        print("Deseas editar el usuario? Si(s) No(n)")
        op = input("Ingresa tu opcion: ")
        if op.lower() == "s":
            edit_user = editUser()
            find_user['name'] = edit_user["name"]
            find_user['last_name'] = edit_user["last_name"]
            find_user['number_phone'] = edit_user["number_phone"]
            find_user['email'] = edit_user["email"]
            print("Usuario editado con exito")
    else:
        return "No se encontro usuario con ese id"


def menu(users = [], ids = []):
    #os.system("clear")
    print("Menu: \n(1)Deseas registrar nuevos usuarios? \n(2)Deseas mostrar todos los ides de los usuarios? \n(3)Deseas mostrar los datos de un usuario por su id?")
    option = int(input("Ingresa tu opcion: "))
    
    if option == 1:
        n = int(input("Cuantos usuarios deseas registrar: "))
        for i in range(n):
            ids.append(idsAdd(i+1))
            users.append(register(i+1, ids[i]))
            print(f"El Usuario {i+1} ha sido registrado con exito!!!!!")
            print(f"En breve recibira un correo a {users[i]['email']}\n")
    elif option == 2:
        for id in ids:
            print(id)
    elif option == 3:
        id = input("Ingresa el id del usuario: ")
        findUserById(users, id)
    else:
        print("Ingresa una opcion valida")
        return menu(users, ids)

    print("Deseas volver al menu?")
    continue_ = input("Ingresa 'S' o 'N': ")
    return menu(users, ids) if continue_.upper() == "S" else exit


def main():
    users = []
    ids = []
    menu(users, ids)
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
