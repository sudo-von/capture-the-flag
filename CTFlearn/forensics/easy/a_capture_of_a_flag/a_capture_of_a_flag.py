# Importo base64.
import base64
# Mensaje secreto que ingresará el usuario en base64.
secret_message = input('Escribe el mensaje encriptado: \n')
# Mensaje desencriptado.
print('Este es el mensaje desencriptado: {}'.format(base64.b64decode(secret_message)))
