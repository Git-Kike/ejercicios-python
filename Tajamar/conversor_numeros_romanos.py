# Conversor de número romanos a decimal teniendo en cuenta que los números romanos se escriben con letras mayúsculas y no se pueden repetir más de 3 veces seguidas.

def convertir_romano_a_decimal(romano):
        
        valores = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        decimal = 0
        anterior = 0
        repeticiones = 0
        
        for letra in romano:
            
            valor = valores[letra]
            
            if valor > anterior:
                decimal += valor - 2 * anterior
                repeticiones = 0
            else:
                if valor == anterior:
                    repeticiones += 1
                    if repeticiones > 2:
                        return "Número romano no válido."
                else:
                    repeticiones = 0
                decimal += valor
            
            anterior = valor
        
        return decimal

romano = input("Introduce un número romano: ")
resultado = convertir_romano_a_decimal(romano)

print(resultado)

