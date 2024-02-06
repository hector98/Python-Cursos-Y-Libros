def userNew(name, last_name, email):
    return f"Hola {name} {last_name} en breve recibirás un correo a {email}"


def main():
    name = input("Ingresa tu nombre: ")
    last_name = input("Ingresa tu apellido: ")
    number_phone = int(input("Ingresa tu numero de telefono: "))
    email = input("Ingresa tu correo electronico: ")
    print(userNew(name, last_name, email))


if __name__ == "__main__":
    main()
