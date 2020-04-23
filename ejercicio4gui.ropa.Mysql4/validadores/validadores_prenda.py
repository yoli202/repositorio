import re

expresion_prenda = "^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]{2,20}$"
expresion_talla = "^[0-9]{1,5}$"
expresion_color = "^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]{2,20}$"
expresion_temporada = "^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]{2,20}$"
#expresion_precio = "^[0-9]{1,7}$"

def validar_prenda(prenda):
    validador = re.compile(expresion_prenda)
    return validador.match(prenda)
def validar_talla(talla):
    validador = re.compile(expresion_talla)
    return validador.match(talla)
def validar_color(color):
    validador = re.compile(expresion_color)
    return validador.match(color)
def validar_temporada(temporada):
    validador = re.compile(expresion_temporada)
    return validador.match(temporada)
#def validar_precio(precio):
    #validador = re.compile(expresion_precio)
    #return validador.match(precio)
