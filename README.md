# api_django

### Inicio

#para crear la api primero hacer pip install virtualenv
#luego python -m venv ["nombre de la carpeta o proyecto"]
#en vs code ctrl + mayus + p --> y en esa consola, escribir Python selected interpreter --> hacer click ->elegir la version de py que # #queremos (esta version va a ser utilizada solo para este proyecto) (por lo gral se elije la que tiene una estrella)

### Instalacion de Django

#pip install django
#para ver si quedo instalado django-admin --version o python -m django --version
#tambien podemos escribir python
#import django
#django.getversion()
#para salir de la shell de django exit()

### Crear proyecto

#django-admin startproject "nombre_del_proyecto"
#para "emprolijar" el proyecto --> django-admin startproject "nombre_del_proyecto" . (el punto pone la carpeta en la raiz sin crear una #nueva

### Correr el servidor

#python manage.py runserver
#si sale Starting development server at http://127.0.0.1:8000/ quiere decir que la web esta corriendo ahi correctamente
#NOTAR que creo un archivo db.sqlite3 que es la BBDD local por defecto
#si quiero elegir el puerto para desplegar python manage.py runserver "numero_puerto"

### Ayuda

#python manage.py --help

### Estructura de un proyecto

#init.py --> solo dice que es un proyecto django

#settings.py --> sirve para configurar el proyecto (similar al ENV de symfony)
#dentro de esta, esta allow host que da permisos de acceso al proyecto
#debug sirve para correr de manera locao-> al llefvar a produccion poner en false
#secrert key es una clave para encriptar datos
#base_dir sirve para determinar la carpeta base del proyecto
#installed_apps -> sirve para ver cuantas aplicaciones tengo creadas (son las divisiones que se hace en el proyecto)
#databases indica a que base de datos estamos conectados
#timezone establece el horario
#languaje idiomas en caso de querer establecerlos
#static url sirve para determinar donde estan los archivos estaticos (html, js y css dentro de una carpeta static)

#archivo urls.py
#se escriben las url o rutas que los usuarios pueden ingresar

#archivo asgi.py y wsgi.py
#sirve para determinar como se va a ejecutar el proyecto, es decir como se va a servir el contenido en producción

# App

#Cada parte del proyecto se considera una app (por ejemplo usuarios, productos, etc)
#para crear una aplicacion python manage.py startapp "nombre_seccion"
#ingresamos a la carpeta raiz y podemos hacer las configuraciones necesarias

# Views

#dentro de la aplicacion hay un archivo que se llama views.py (html)

#migrations se va llenando con los datos de la bbdd, django utiliza ORM para acceder a la bbdd
#si necesitamos una operacion compleja se puede hacer una consulta sql

#el archivo admin.py --> tiene un panel administrador con el que podemos manejar los datos

#apps.py --> sirve para configurar la sección

#models.py --> sirven para crear las clases que se utilizan en el ORM

#test.py --> sirven para crear los test de las vistas o de la app

# Primer mensaje que se retorna al navegador

#Se hace dentro de la aplicacion que queramos -> views -> creamos una funcion de retorno
#Luego vamos a mysite/urls.py y agregamos la ruta de la respuesta
#PAra enviar un elemento html , ver en views
#Para mejorar las url , necesitamos crear un archivo urls.py en la carpeta del proyecto utilizando include en estamos_todos/urls.py

# Para realizar migraciones (BBDD)

#python manage.py makemigrations
#python manage.py migrate ->ejecuta las migraciones creando las tablas por defecto dentro de la bbdd

#para crear una tabla en bbdd debemos crear un modelo en models.py dentro del proyecto
#luego para actualizar la bbdd se debe conectar desde estamos_todos/settings.py INSTALLED_APP
#despues hacemos unas nuevas migraciones con python manage.py makemigrations o python manage.py makemigrations myapp
#finalmente python manage.py migrate myapp
