
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
    ids = num_user * 19981205
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


def main():
    n = int(input("Cuantos usuarios deseas registrar: "))
    users = []
    ids = []

    for i in range(n):
        ids.append(idsAdd(i+1))
        users.append(register(i+1, ids[i]))
        print(f"El Usuario {i+1} ha sido registrado con exito!!!!!")
        print(f"En breve recibira un correo a {users[i]['email']}\n")

    print("Los ids de los usuarios registrados son: ")
    print(ids)

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
