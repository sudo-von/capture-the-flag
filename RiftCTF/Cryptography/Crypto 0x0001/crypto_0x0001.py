# -*- coding: utf-8 -*- 
# Importo base64 y binascii.
import base64
import binascii

# Función para decodificar un base64 recursivamente hasta que ya no se pueda más.
def is_base64(s):
    # Mientras se pueda decodificar se seguirá llamando recursivamente.
    try:
        # Imprimo el resultado de la decodificación.
        print(base64.decodestring(s))
        # Llamada recursiva.
        is_base64(base64.decodestring(s))
    # Cuando no se pueda más saldrá de la función con el return.
    except binascii.Error:
        return False

# Se manda a llamar la función que recibe como parámetro el mensaje codificado en baset64.
is_base64('V1RJeGMySlhVa1pVYkZaVFltNVNTMXBGYUU5YWF6VkdaVVV4V1UxclduQlVWV2hYVFVabmQxTnRhRlpsYXpRMQ==')
