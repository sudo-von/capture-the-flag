### POST Practice

#### 40 Points
Descripción del reto:

These website requires authentication, via POST. However, it seems as if someone has defaced our site.
Maybe these is still some way to authenticate?


#### URL del reto
	http://165.227.106.113/post.php

### Solución del reto

Al ingresar al sitio, indica que hay información mediante una petición POST que no ha sido enviada, pero como siempre menciono, lo que haremos antes de continuar es inspeccionar la página.
[![Imagen inicial del reto](Imagen del sitio que nos muestra el reto "Imagen reto")](https://i.imgur.com/Wq4kTtp.png "Imagen reto")

Siempre en cada reto que sea web, lo primero que debemos hacer es dar en inspeccionar elemento, puesto que muchas veces encontraremos información en el código que ahí nos muestran.

En este caso nos muestra:
	#<h1>This site takes POST data that you have not submitted!</h1><!-- username: admin | password: 71urlkufpsdnlkadsf -->
	

Esto será importante para la herramienta que utilizaremos, se llama Postman
`https://www.getpostman.com/`

La instalamos y la pantalla inicial cuando abrimos una nueva pestaña será la siguiente:
[![Imagen aplicativo postman](aplicativo postman "Imagen aplicativo postman")](https://i.imgur.com/qGo0EFi.png "Imagen aplicativo postman")

El siguiente paso es cambiar el GET por el POST, y en el formulario de "body", vamos a "form-data", allí pondremos los parametros de username y password como lo muestro en la siguiente imagen:
[![Como configurar el postman](Imagen de como configurar el postman "Postman")](https://i.imgur.com/vNtzOEo.png "Postman")

Y listo, tendremos nuestra flag para poder presumirla con nuestro crush y que así te elija a ti por encima de cualquier otro, porque obviamente, quien no quiere tener a alguien que sabe hacer un ataque POST en los formularios, mucha suerte y la flag se muestra de la siguiente forma:

[![Flag del reto](Flag del reto "Flag del reto")](https://i.imgur.com/IT5QmqE.png "Flag del reto")
