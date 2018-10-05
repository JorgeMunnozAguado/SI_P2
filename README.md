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

2) Instalar Apache

	Haremos uso de Apache en su versión 2, por lo que lo instalaremos:
	```
	sudo apt install apache2
	```

	Una vez instalado podremos probarlo, accediendo a la dirección `http://localhost`.

3) Unir Apache y python.

	Para hacer uso de las dos herramientas utilizaremos el módulo `wsgi`, el cual habrá que activa en nuestro linux.
	```
	apt-get install libapache2-mod-wsgi
	```

Una vez instalados los anteriores paquetes toca configurar el servidor.
Los siguientes pasos los hemos realizado con la ayuda de la página <https://tecadmin.net/install-apache-mod-wsgi-on-ubuntu-18-04-bionic/>

1) En primer lugar vamos a crear un nuevo sitio web.

	Para ello debemos ejecutar los siguientes comandos, cambiando `%name%` por el nombre de la pagina web.
	```
	sudo mkdir /var/www/%name%.com
	cd /var/www/%name%.com
	sudo mkdir /public_html
	sudo chown -R $USER:$USER /public_html
	sudo chmod -R 755 /var/www
	```

2) El siguiente paso será crear un fichero `.wsgi`.
	
	Crearemos un fichero de prueba.

	```
	cd public_html
	vim holaMundo.wsgi
	```

	El cuál contendrá la siguiente información:

	```wsgi
	import os
	import sys

	sys.path.append('/var/www/%name%.com/application')

	os.environ['PYTHON_EGG_CACHE'] = '/var/www/%name%.com/.python-egg'

	def application(environ, start_response):
		status = '200 OK'
		output = 'Hello World!'

		response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
		start_response(status, response_headers)

		return [output]
	```

