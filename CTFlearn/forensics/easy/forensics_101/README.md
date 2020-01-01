# Forensics 101

## 30 points

### Forensics - Easy

Descripción del reto:

```
Think the flag is somewhere in there. Would you help me find it?
```

### URL del archivo:

```
https://mega.nz/#!OHohCbTa!wbg60PARf4u6E6juuvK9-aDRe_bgEL937VO01EImM7c
```

### Solución del reto:
Para este reto sólo se nos brindará una imagen la cual tiene la flag escondida en algún lugar.
Para solucionar el reto habrá que utilizar strings, un comando de linux que retorna cada string
de un archivo, de todas formas te dejaré aquí abajo una descripción breve del comando para que lo conozcas por si no te quedó muy claro:
```
The strings command returns each string of printable characters in files. Its main uses are to determine the contents of and to extract text from binary files (i.e., non-text files).
```
Una vez habiendo utilizado el comando podremos encontrar la flag en la parte inferior.

![Screenshot](images/01.jpg)
