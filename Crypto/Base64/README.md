# Base64

### Resuelto por Manjaro

### Descripcion del Reto

El reto nos decia que accedieramos a un servicio corriendo en ```18.221.44.9:3133```
y nos dan el codigo del servicio:

```python
import socketserver
import base64

with open('flag.txt','r') as f:
    flag = f.readline()

def magic(cryptic):
    return ''.join(c.lower() if c.isupper() else c.upper() if c.islower() else c for c in cryptic)

def bASE64(cadena):
    return str.encode(magic(str(base64.b64encode(cadena))))

def decode_base64(cadena):
    return base64.b64decode(cadena)

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        opcion = 0
        while opcion != 4:
            try:
                self.request.send(b"\r\n##############bASE64##############\r\n")
                self.request.send(b"Selecciona una opcion:\r\n")
                self.request.send(b"1. Codifica cadena\r\n2. Decodifica Base64\r\n3. Obtener bandera\r\n4. Salir\r\n >>>>")
                opcion = int(self.request.recv(1024).strip())
                if opcion == 1:
                    self.request.send(b"\r\nDame algo para codificar: ")
                    to_send = bASE64(self.request.recv(1024).strip())[2:-1]
                    self.request.send(b"\r\nCadena codificada: ")
                    self.request.send(to_send)
                    self.request.send(b"\r\n\r\n")
                elif opcion == 2:
                    try:
                        self.request.send(b"\r\nDame algo para decodificar: ")
                        to_send = decode_base64(self.request.recv(1024).strip())
                        self.request.send(b"\r\nCadena decodificada: ")
                        self.request.send(to_send)
                        self.request.send(b"\r\n")
                    except:
                        self.request.send(b'\r\nOperacion no permitida...')
                        self.request.send(b"\r\n")
                elif opcion == 3:
                    self.request.send(b"\r\nAqui tiene su bandera: ")
                    self.request.send(bASE64(str.encode(flag))[2:-1])
                    self.request.send(b"\r\n")
                elif opcion == 4:
                    self.request.send(b"\r\nHasta pronto...")
                else:
                    self.request.send(b"\r\nOpcion incorrecta...")
                    self.request.send(b"\r\n")
            except:
                self.request.send(b'\r\nOperacion no permitida...')
                self.request.send(b"\r\n")

        
if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 3101

    server = socketserver.ThreadingTCPServer((HOST, PORT), MyTCPHandler)
    server.allow_reuse_address = True
    server.serve_forever()
```

Accediendo a el con netcat ```nc 18.221.44.9 3133``` y eligiendo la tercera opcion, nos regresa un base64:
```AgfJA2rLzNTIyxnLnJrFm3nFzdnTnhmXngqWx2y0yZfSx3a0CJrFyZbTm256nhj9cG==```
pero al tratar de decodificarlo aparece como invalido.

Analizando el codigo del servicio nos damos cuenta que hay una funcion que invierte las mayusculas y minusculas del base64,
aplicando la misma funcion al base64 que nos regresa el servicio ya lo podemos decodificar y nos da la flag:
```hackdef{base64_3s_d3m4s14d0_f4c1l_p4r4_c0m3nz4r}```