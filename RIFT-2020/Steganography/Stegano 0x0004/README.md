# Stegano 0x0004

## Descripción del reto

```
Don't download pirated music guys, it's not respectful towards the artist.
```

## Solución

En este reto se nos daba un archivo llamado chall4.wav el cual pesaba 10mb, algo raro 
a simple vista por lo que procedí a utilizar binwalk para ver si había algún archivo oculto dentre de este.

![Imagen](Images/01.png)

De esta manera me topé con que había un archivo MySQL ISAM index file version 3 dentro del .wav, sin embargo,
esto me pareció extraño al analizar este archivo oculto por lo que supuse que se trataba de un error,
un falso positivo.

![Imagen](Images/02.png)

Después decidí recurrir a lo más básico, utilizar strings y filtrar con grep la palabra rift en busca de la flag
siendo esta la forma más sencilla de resolver el reto.

![Imagen](Images/03.png)
