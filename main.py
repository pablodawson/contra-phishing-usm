import requests
import csv
import random

#inicia contador
enviados=0

#inicia listas vacías
nombres_l=[]
apellidos_l=[]

#crea lista con contraseñas falsas
f = open("pass.txt", "r")
contrasenas=f.read()
contrasenas_l=contrasenas.splitlines()

#crea lista con nombres
with open('hombres.csv', newline='') as nombres:
    reader = csv.reader(nombres, delimiter=' ', quotechar='|')
    for row in reader:
        nombres_l.append(row[0].split(',')[0])

#crea lista con apellidos
with open('apellidos.csv', newline='') as apellidos:
    reader = csv.reader(apellidos, delimiter=' ', quotechar='|')
    for row in reader:
        apellidos_l.append(row[0].split(',')[0])

#link del request
link=""

#envia mails y contraseñas falsas aleatorias hasta que se pare. cambiar el algoritmo de "contraseña" de vez en cuando para que sea mas dificil de identificar.
while True:
    enviados+=1
    nombre=random.choice(nombres_l).lower()
    apellido=random.choice(apellidos_l).lower()
    contrasena=str(random.randint(0,1000))+str(random.randint(0,1000))+random.choice(nombres_l)
    mail=nombre+"."+apellido+"@usm.cl"

    datos= {
        'username': mail,
        'passwd': contrasena,
        'persist': '0',
    }
    response=requests.post(link, data=datos).text
    print(str(enviados))
