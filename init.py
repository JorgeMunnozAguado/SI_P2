from flask import Flask, render_template, send_from_directory, request, redirect, make_response
import datetime
from pelicula import Pelicula
from utilficheros import jsonAPelicula, resultadoPeliculas, searchFilms
import os
import json

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():

    if "SessionCookie" in request.cookies:

        # Comprobar sesion
        if request.cookies.get('SessionCookie') == "admin":
            return redirect("/last")

        else:
            return "SESION"

    else:

        if request.method == 'POST':

            username = request.form['username']
            password = request.form['password']

            if username == "admin" and password == "admin":

                expire_date = datetime.datetime.now()
                expire_date = expire_date + datetime.timedelta(hours = 1)

                resp = make_response(redirect("/last"))
                resp.set_cookie('SessionCookie', username, expires = expire_date)
                return resp

            else:
                return render_template("index-fail.html")

        else:
            return render_template("index.html")

@app.route("/last")
def last():
    json_url = os.path.join(SITE_ROOT, "data", "catalogo.json")
    pelis=jsonAPelicula(json_url)
    return checkSessionPelis("last.html",pelis)

@app.route("/fullFilm/<name>")
def fullFilm(name):
    json_url = os.path.join(SITE_ROOT, "data", "catalogo.json")
    pelis=jsonAPelicula(json_url)
    for peli in pelis:
        if name == peli.link:
            return checkSessionPelis("fullFilm.html",peli)
    return redirect('/last')

@app.route("/basket")
def basket():

    if "basket" in request.cookies and "SessionCookie" in request.cookies:

        cookie = request.cookies.get('basket')
        obj = json.loads(cookie)

        buscar = obj["films"]

        json_url = os.path.join(SITE_ROOT, "data", "catalogo.json")
        pelis = jsonAPelicula(json_url)

        ret = searchFilms(buscar, pelis)

        return render_template("basket.html", films = ret[0], precioTotal = ret[1])

    elif "SessionCookie" in request.cookies:
        return checkSession("basket.html")
        
    else:
        return redirect("/")

@app.route("/history")
def history():
    return checkSession("history.html")

@app.route("/sing_up")
def registro():
    if 'ccv' in request.form:
        if request.method == 'GET':
            nombre=request.args.get('nombre')
    		dict_res['nombre']=nombre
            dict_res['password']=request.args.get('password')
            repite=request.args.get('repite')
            dict_res['email']=request.args.get('email')
            dict_res['tarjeta']=request.args.get('tarjeta')
            dict_res['titular']=request.args.get('titular')
            dict_res['ccv']=request.args.get('ccv')
            dict_res['mes']=request.args.get('mes')
            dict_res['anno']=request.args.get('anno')
            user_url = os.path.join(SITE_ROOT, "users","info", str(nombre))
            if crearDatosUsuario(user_url,dict_res) == True:
                return 
            else:
                return render_template("registro.html")
        elif request.method == 'POST':
	        nombre=request.form['nombre']
            dict_res['nombre']=nombre
            dict_res['password']=request.form['password']
            repite=request.form['repite']
            dict_res['email']=request.form['email']
            dict_res['tarjeta']=request.form['tarjeta']
            dict_res['titular']=request.form['titular']
            dict_res['ccv']=request.form['ccv']
            dict_res['mes']=request.form['mes']
            dict_res['anno']=request.form['anno']
            user_url = os.path.join(SITE_ROOT, "users","info", str(nombre))
            if crearDatosUsuario(user_url,dict_res) == True:
                return 
            else:
                return render_template("registro.html")
        else:
            return render_template("registro.html")
    else:
        return render_template("registro.html")


@app.route("/search", methods=['POST','GET'])
def search():
    json_url = os.path.join(SITE_ROOT, "data", "catalogo.json")
    pelis=jsonAPelicula(json_url)
    if request.method == 'GET':
        search=request.args.get('search')
        tipo=request.args.get('programa')

        return checkSessionPelis("search.html",peliculas=resultadoPeliculas(search,tipo,pelis))
    elif request.method == 'POST':
        search=request.form['search']
        tipo=request.form['programa']

        return checkSessionPelis("search.html",peliculas=resultadoPeliculas(search,tipo,pelis))
    else:
        return redirect(url_for('last'))

@app.route("/close")
def closeSession():

    if "SessionCookie" in request.cookies:

        # Creo que no hay que hacer mas comprobaciones

        resp = make_response(redirect("/"))
        resp.set_cookie('SessionCookie', '', expires = 0)
        return resp

    else:
        return redirect("/")



@app.route('/images/<path:path>')
def send_images(path):
    return send_from_directory('static/images', path)

@app.route('/styles/<path:path>')
def send_styles(path):
    return send_from_directory('templates/styles', path)

@app.route('/scripts/<path:path>')
def send_scripts(path):
    return send_from_directory('templates/scripts', path)

def checkSession(url):

    if "SessionCookie" in request.cookies:
        return render_template(url)
    else:
        return redirect("/")

def checkSessionPelis(url,peliculas):

    if "SessionCookie" in request.cookies:
        return render_template(url,peliculas=peliculas)
    else:
        return redirect("/")

if __name__ == "__main__":
    app.run()

