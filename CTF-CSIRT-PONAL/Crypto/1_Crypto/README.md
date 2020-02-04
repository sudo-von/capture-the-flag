# 1_Crypto

## Descripción del reto

```
HORWRUULQRODULQJRORJRGHSDUDQJDULFXWLULPLFXDUR
```

## Pista

```
La palabra que encuentras es, sin embargo, existen diversas formas de escribirla. Lograrás encontrar la forma correcta. 
```

## Solución

En este reto nos daban un mensaje cifrado sin más, por lo que lo primero que pensé fue en utilizar Caesar Cipher el cual
es un cifrado por desplazamiento, siendo este una de las técnicas de cifrado más simples y usadas.

![Caesar Cipher](Images/01.png)

Efectivamente obtuvimos un mensaje, sin embargo, la plataforma indicaba que esa no era la flag, y después de ver la pista
me quedaba claro que sí era ese el mensaje, pero no estaba escrito como la plataforma quería así que elaboré un script en python muy sencillo
para pasar el mensaje de mayúsculas a minúsculas obteniendo así la flag correcta.

![Script de Python](Images/02.png)
