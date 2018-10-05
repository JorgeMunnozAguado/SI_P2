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

3) Unir Apache y python con el módulo `wsgi`.

	Para hacer uso de las dos herramientas utilizaremos el módulo `wsgi`, el cual habrá que activa en nuestro linux.
	```
	apt-get install libapache2-mod-wsgi
	```

Una vez instalados los anteriores paquetes toca configurar el servidor.
Los siguientes pasos los hemos realizado con la ayuda de la página <https://tecadmin.net/install-apache-mod-wsgi-on-ubuntu-18-04-bionic/>

1) En primer lugar, debemos copiar el repositorio, entrega a la carpeta `/var/www`.

2) El siguiente paso será modificar la configuración de Apache para que utilice el módulo `wsgi`.
	
	
	Debemos abrir el siguiente archivo:
	```
	sudo vim /etc/apache2/conf-available/mod-wsgi.conf
	```

	A continuación, insertamos el siguiente código:
	```
	WSGIScriptAlias / /var/www/html/server.py
	```

3) Por último, solo necesitamos reiniciar Apache.

	```
	sudo a2enconf mod-wsgi
	sudo systemctl restart apache2
	```

