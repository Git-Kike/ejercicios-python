# Simulador de dados

import random
class Dado:
    def __init__(self, numero_caras: int):
        if numero_caras < 1:
            raise ValueError("Este numero de caras es incorrecto")
        self.numero_caras = numero_caras
        
    def tirada(self) -> int | None:
        valor_tirada = random.randint(1, self.numero_caras)
        print(f"Se ha hecho una tirada y ha salido {valor_tirada}")
        return valor_tirada


mi_dado = Dado(6)

mi_dado.tirada()