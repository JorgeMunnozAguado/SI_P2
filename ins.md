sudo apt install apache2
> http://localhost

sudo apt install python-pip virtualenv

sudo su

cd /etc/apache2/sites-available/

vim flask.conf

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

apt install libapache2-mod-wsgi

cd /var/www/
mkdir flask
cd flask/
mkdir static templates

virtualenv venv

vim init.py

```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

if __name__ == "__main__":
    app.run()
```

pip install flask

python init.py

> http://localhost:5000

vim flask.wsgi

```
import sys

sys.path.insert(0, "/var/www/flask/")

from init import app as application
```

a2ensite flask.conf
a2dissite 000-default.conf
systemctl reload apache2

