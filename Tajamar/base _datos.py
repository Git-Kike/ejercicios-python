# Crear un programa que funcione como una base de datos donde se pide un nombre de usuario y una contraseña, y si la contrasña es valida, se almacena el usuario y la contraseña en un diccionario y se genera un archivo .txt


def validar_contraseña(contraseña):
     
        requisitos_faltantes = []
        
        if len(contraseña) < 8:
            requisitos_faltantes.append("tener al menos 8 caracteres")
        
        if not any(char.islower() for char in contraseña):
            requisitos_faltantes.append("contener al menos una letra minúscula")
            
        if not any(char.isupper() for char in contraseña):
            requisitos_faltantes.append("contener al menos una letra mayúscula")
        
        if not any(char.isdigit() for char in contraseña):
            requisitos_faltantes.append("contener al menos un dígito")
        
        if not any(char in "!@#$%^&*(),.?\":{}|<>" for char in contraseña):
            requisitos_faltantes.append("contener al menos un carácter especial")
        
        if requisitos_faltantes:
            return "La contraseña no es válida. Requisitos faltantes: " + " / ".join(requisitos_faltantes) + "."
        else:
            return "La contraseña es válida."
        
def guardar_usuario(usuario, contraseña):
    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{usuario} {contraseña}\n")

usuarios = {}

while True:
    usuario = input("Introduce un nombre de usuario: ")
    contraseña = input("Introduce una contraseña: ")
    
    resultado = validar_contraseña(contraseña)
    
    if resultado == "La contraseña es válida.":
        guardar_usuario(usuario, contraseña)
        usuarios[usuario] = contraseña
        print("Usuario registrado correctamente.")
    else:
        print(resultado)
        break
    
    continuar = input("¿Quieres registrar otro usuario? (s/n): ")
    
    if continuar.lower() != "s":
        break









