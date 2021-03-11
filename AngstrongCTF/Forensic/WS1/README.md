# ws1

## Descripción del reto

```
Find my password from this recording (:
```

## Solución

En este reto nos daban un archivo llamado recroding.pcapng, un archivo
que por su extensión se deduce que habrá que utilizar wireshark, un analizador
de paquetes.

![Paquetes](Images/01.png)

Una vez analizado el paquete basta con ordenar las peticiones mediante el filtro de protocolos,
aquí nos encontraremos con dos peticiones HTTP las cuales como se podrán imaginar no están cifradas.

Al analizar la información que viajó a través de dicha petición encontraremos la flag, sin embargo,
aún falta decodificar el mensaje pues está codificado con el formato de URL.

![Paquetes](Images/02.png)

Después de ir a cualquier página para decodificar el formato URL obtendremos la flag.

![Flag](Images/03.png)
