# ninjablog
Para instalar la aplicación en modo desarrollo debera seguir los siguientes pasos:
===========================================================

1-) Instalar el controlador de versiones git:
------------------------------------------------------
    
    Ingresar como super usuario:

    $ su

    # aptitude install git
    
    Salir del modo super usuario

2-) Descargar el codigo fuente del proyecto:

$ git clone https://github.com/carlosnp/ninjablog.git

3-) Crear un Ambiente Virtual:
El proyecto está desarrollado con el lenguaje de programación Python, se debe instalar Python 3.6.7

4.- Luego de instalar el ambiente virtual:

$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver