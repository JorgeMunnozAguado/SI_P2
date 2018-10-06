# Instalación

1) Instalar python.

	En este caso haremos uso de `python 2.7`.
	```
	sudo apt install python2.7
	```
	También deberemos tener `pip` instalado.
	```
	sudo apt install pip
	```
	Para que podamos instalar la librería `Flask` para Python.
	```
	pip install flask
	```


2) Instalar Apache

	Haremos uso de Apache en su versión 2, por lo que lo instalaremos:
	```
	sudo apt install apache2
	```

	Una vez instalado podremos probarlo, accediendo a la dirección `http://localhost`.


	Instalaremos también el host virtual:
	```
	sudo apt install virtualenv
	```

3) Unir Apache y python con el módulo `wsgi`.

	Para hacer uso de las dos herramientas utilizaremos el módulo `wsgi`, el cual habrá que activa en nuestro linux.
	```
	apt-get install libapache2-mod-wsgi
	```

Una vez instalados los anteriores paquetes toca configurar el servidor.
Para ayudarnos con la instalación y puesta en marcha del servidos, nos hemos apoyado en el video:  <https://www.youtube.com/watch?v=wq0saslschw>

1) En primer lugar, debemos configurar Apache.

	Para ello debemos acceder a la siguiente carpeta. Es recomendable acceder como `root` con el comando `sudo su`.
	```
	cd /etc/apache2/sites-available/
	```

	Crearemos el fichero `SI_P2.conf` el cuál contedrá la configuración de nuestro host virtual:

	```conf
	<VirtualHost *:80>

        	serverName      flaskapp.com
	        WSGIScriptAlias / /var/www/flask/flask.wsgi

        	<Directory /var/www/flask>

                	Order allow,deny
	                Allow from all

        	</Directory>

	        ErrorLog ${APACHE_LOG_DIR}/error.log
        	CustomLog ${APACHE_LOG_DIR}/error.log combined

	</VirtualHost>
	```


2) A continuación, deberemos copiar el repositorio, entrega, a la carpeta `/var/www`.

	Esta carpeta, con nombre `SI_P2` cuenta con el archivo `init.py`, el cual contiene la aplicación Flask.

	Además, esta carpeta cuenta con además con el archivo `server.wsgi`, el cual contiene la siguiente información:

	```python
	import sys

	sys.path.insert(0, "/var/www/SI_P2/")

	from init import app as application
	```

3) Por último, debemos mostrar a Apache2 la configuración realizada.

	Con los siguientes comandos pediremos a Apache que habilite nuestra página web y desabilite la que se encuentra por defecto. Además, reiniciamos el servidor Apache para que carge la nueva configuración.
	```
	a2ensite SI_P2.conf
	a2dissite 000-default.conf
	systemctl reload apache2
	```

Una vez seguidos estos pasos podremos acceder a nuestra página web a través de la direccion `http://localhost`.

