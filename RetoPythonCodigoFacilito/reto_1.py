def userNew(name, last_name, email):
    return f"Hola {name} {last_name} en breve recibirás un correo a {email}"


def validates(field, len_min, len_max, name_field):
    if len(field) >= len_min and len(field) <= len_max:
        return field
    else:
        print(f"El {name_field} debe tener entre {len_min} y {len_max} caracteres")
        field = input(f"Ingresa su {name_field}: ")
        return validates(field, len_min, len_max, name_field)
    

def register(num_user):
    print(f"Ingresa los datos del Usuario {num_user}")
    name = validates(input("Ingresa su nombre: "), 5, 50, "nombre")
    last_name = validates(input(f"Ingresa su apellido: "), 5, 50, "apellido")
    number_phone = validates(input("Ingresa su numero de telefono: "), 10, 10, "numero de telefono")
    email = validates(input("Ingresa su correo: "), 5, 50, "email")

    user = {
        "name": name,
        "last_name": last_name,
        "number_phone": number_phone,
        "email": email
        }
    return user


def main():
    n = int(input("Cuantos usuarios deseas registrar: "))
    users = []

    for i in range(n):
        users.append(register(i+1))
        print(f"El Usuario {i+1} ha sido registrado con exito!!!!!")
        print(f"En breve recibira un correo a {users[i]['email']}\n")

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
