# Ladybug

![CTF](img/1.jpg)

De entrada era una página normal donde podías navegar entre diferentes categorías.

![CTF](img/2.jpg)

Después de hacer el recorrido por toda la página no encontré nada interesante por lo que decidí
acceder mediante la URL a algún recurso diferente de los mostrados.

![CTF](img/3.jpg)

Así fue como me topé con algo muy interesante. El sitio web fue hecho con Flask, un framework de Python.

![CTF](img/4.jpg)

Cuando navegué más abajo noté que se mencionaba un debugger así que me puse a investigar más acerca de esto.

![CTF](img/5.jpg)

Este mensaje se muestra debido a que al levantar el servidor se dejó el parametro de debug como True, y esto
supone un gran peligro pues sólo debe ser usado en desarrollo pero no en producción.

![CTF](img/6.jpg)

Werkzeug es una librería que permite hacer pruebas de muchos tipos.

![CTF](img/7.jpg)

Así que navegué a la consola de Werkzeug ubicada en /console.
Aquí se mencionaba que podías ejecutar expresiones de Python en el contexto de la aplicación.

![CTF](img/8.jpg)

Ya en este punto fue bastante sencillo obtener la flag, tan sólo creé un payload utilizando los subprocesos
de Python para ejecutar el comando ls para listar los archivos y luego usar el comando cat para traerme
el contenido de la bandera.

![CTF](img/9.jpg)

![VON](../../von.jpg)