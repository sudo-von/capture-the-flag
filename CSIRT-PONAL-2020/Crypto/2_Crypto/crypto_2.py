# -*- coding: utf-8 -*-
# Importo MySQL connector para conectarme a la base de datos y ejecutar la función SELECT CHAR.
import mysql.connector as mysql
# Configuración de la base de datos.
db = mysql.connect(host="localhost", user="", passwd="")
# Cursor.
cur = db.cursor()
# Información cifrada.
informacion_cifrada = '069108 109117110100111 101115116225 108108101110111 100101 109105115116101114105111115044 101110 101115116101 099097115111 116117 114101115112117101115116097 101115 034070076065071045067083049082084080048078052076034 115105110 099111109105108108097115046'.split(' ')
# Ciclo para iterar  a través de la lista de información cifrada.
for i in range(0,len(informacion_cifrada)):
    # Preparo la consulta a la base de datos.
    consulta = 'SELECT CHAR('
    # Variable temporal.
    temporal = informacion_cifrada[i]
    # Ciclo para iterar a través de los valores de la variable temporal.
    for j in range(1,len(temporal)+1):
        # Esto me permitirá generar las comas correspondientes que pide la función como parte del delimitador de los argumentos.
        # Ejemplo: SELECT CHAR(100,110,105);
        # Condición para lograr este efecto.
        if j%3 == 0 and j < len(temporal):
            consulta += '{},'.format(temporal[j-1])
        else:
            consulta += temporal[j-1]
    # Cierro la consulta.
    consulta += ');'
    # Ejecuto la consulta.
    cur.execute(consulta)
    # Guardo la flag.
    flag = cur.fetchone()[0]
    # Imprimo la flag.
    print(flag.decode('cp1252'))

# Cierro la conexión.
db.close()
