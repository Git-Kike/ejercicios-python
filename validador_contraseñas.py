#Validador de contraseña

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
        return "La contraseña no es válida: debe " + " / ".join(requisitos_faltantes) + "."
    else:
        return "La contraseña es válida."


contraseña = input("Introduce una contraseña: ")
resultado = validar_contraseña(contraseña)
print(resultado)
