# Base64

### Resuelto por Manjaro

### Descripcion del Reto

En este reto nos dan un exe al cual le podemos pasar un string para que nos lo codifique,
y nos dan un archivo *secreto* que se supone que es la flag codificada:

```2E62DD6F7BE9BDB80322DBEF52ECA8360E4E9CDABDA85D0936683EB7CE41CE91E6CCDFA433C3BB3F```

Naturalmente, intentamos decompilar el exe para ver el codigo y revertir el proceso de encriptacion.
Luego pense:
Y al pasarle *"hackdef{"* al exe y compararlo con los primeros digitos de *secreto* resultaron ser iguales.

### Solucion

Cree un script en python para bruteforcearlo, basicamente añadiendo un caracter y comparando el resultado de la encriptacion
con el *secreto* hasta que el string sea igual al codificado. (el script cambia un poco para windows o linux, pero la logica es igual)

```python
import string
import subprocess
import os

os.chdir('/home/mario/Documents/ctf/hackdef2018/quals/4cr')
chars = '.-_}'+string.ascii_letters+string.digits#string.printable //windows
f = open('secret').read()

flag = 'hackdef{'

for i in range(30):
    for c in chars:
        #r = subprocess.run(['C2C_module.exe', flag+c], stdout=subprocess.PIPE).stdout.decode('utf-8') //windows
        p = subprocess.Popen(['wine C2C_module.exe '+flag+c],shell=True,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
        r, err = p.communicate()
        p.terminate()
        if r.decode('utf-8') in f:
            flag = flag+c
            print(flag)
            if '}' in flag:
                quit()
print(flag)
```

Y sacamos la flag ```hackdef{RC4_is_c0mm0nly_used_by_m4lwar3}```