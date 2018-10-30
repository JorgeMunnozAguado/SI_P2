from flask import Flask, session, render_template, send_from_directory, request, redirect, make_response
from pelicula import Pelicula
from utilficheros import jsonAPelicula, resultadoPeliculas, searchFilms, peliculaEnCarrito
from users import Users
import os
import sys
import json
import time
import md5
import random

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))

app = Flask(__name__)


app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' #EJEMPLO

try:
    from flask_session import Session
    
    this_dir = os.path.dirname(os.path.abspath(__file__))
    SESSION_TYPE = 'filesystem'
    SESSION_FILE_DIR = this_dir + '/sessions'
    SESSION_COOKIE_NAME = 'SessionCookie'
    app.config.from_object(__name__)
    Session(app)
    
    print >>sys.stderr, "Usando sesiones de Flask-Session en fichero del servidor"
    
except ImportError as e:
    print >>sys.stderr, "Flask-Session no disponible, usando sesiones de Flask en cookie"



@app.route("/",methods=['GET', 'POST'])
def index():
    json_url = os.path.join(SITE_ROOT, "data", "catalogo.json")
    pelis = jsonAPelicula(json_url)
    return checkSessionPelis("last.html", pelis,False)


@app.route("/login", methods=['GET', 'POST'])
def login():

    if "SessionCookie" in request.cookies:

        if 'username' in session and 'password' in session:

            if Users.checkUser(session['username'], session['password']):
                return redirect("/")
                

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']
        
        m = md5.new()
        m.update(str(password))
        password = m.hexdigest()

        if Users.checkUser(username, password):

            resp = make_response(redirect("/"))
            
            session['username'] = username
            session['password'] = password
            
            return resp

        else:
            return render_template("index-fail.html")


    return render_template("index.html")

@app.route("/fullFilm/<name>")
def fullFilm(name):

    json_url = os.path.join(SITE_ROOT, "data", "catalogo.json")
    pelis = jsonAPelicula(json_url)
    
    for peli in pelis:
        if name == peli.link:
            return checkSessionPelis("fullFilm.html", peli,False)
            
    return redirect('/')


@app.route("/basket")
def basket():

    if "SessionCookie" in request.cookies:
    
        if "basket" in session:
        
            obj = json.loads(session['basket'])
                            
            buscar = obj["films"]

            ret = searchFilms(buscar)
        
            if 'username' in session and 'password' in session:

                if Users.checkUser(session['username'], session['password']):

                    return render_template("basket.html", films = ret[0], precioTotal = ret[1], user=session['username'])
                
            else: return render_template("basket.html", films = ret[0], precioTotal = ret[1])
            
        return checkSession("basket.html")
    
    return redirect("/")


@app.route("/pay", methods=['POST','GET'])
def pay():

    if "SessionCookie" in request.cookies:
    
        if 'username' in session and 'password' in session and 'basket' in session:

            if Users.checkUser(session['username'], session['password']):
            
                user = Users.getUserFromDB(session['username'])
                obj = json.loads(session['basket']) ## HACER MAS BONITO
                
                if request.method == 'POST':
                
                    if Users.buyFilm(user, session['basket']) == True:
                        session['basket'] = json.dumps({'films':[]})
                        return redirect("/history")
                    
                    else:
                    
                        buscar = obj["films"]
                        ret = searchFilms(buscar)
                    
                        return render_template("pay-fail.html", user=user, date=time.strftime("%d/%m/%y"), price=ret[1])
                    
                    
                buscar = obj["films"]
                ret = searchFilms(buscar)
                
                return render_template("pay.html", user=user, date=time.strftime("%d/%m/%y"), price=ret[1])
            
        
            return render_template("pay.html")
            
    return redirect("/")
    

@app.route("/history")
def history():

    if "SessionCookie" in request.cookies:
    
        if 'username' in session and 'password' in session:

            if Users.checkUser(session['username'], session['password']):
            
                return render_template("history.html", peliculas=Users.listUserFilms(session['username']), user=session['username'])
    
    return redirect("/")


@app.route("/sing_in",methods=['GET','POST'])
def registro():
    if 'tarjetaValor' in request.form:
        if request.method == 'GET':
            nombre=request.args.get('nombre').lower()
            password=request.args.get('password')
            if Users.getUserFromDB(nombre) != None:
                return render_template("registro.html",msg="Nombre de usuario ya registrado")
            if Users.createNewUser(request.args.get('nombre').lower(), request.args.get('password'),request.args.get('tarjetaValor'), 0,request.args.get('email')) == None:
                return render_template("registro.html",msg="Error al crear el usuario")
            else:
                if Users.checkUser(nombre,password):
                    resp = make_response(redirect("/"))
            
                    session['username'] = nombre
                    session['password'] = password
            
                    return resp
                else:
                    return render_template("index.html")
        elif request.method == 'POST':
            nombre=request.form['nombre'].lower()
            if Users.getUserFromDB(nombre) != None:
                return render_template("registro.html",msg="Nombre de usuario ya registrado")
            password=request.form['password']
            if Users.createNewUser(request.form['nombre'].lower(), request.form['password'], request.form['tarjetaValor'], 0, request.form['email']) == None:
                return render_template("registro.html",msg="Error al crear el usuario")
            else:
                if Users.checkUser(nombre,password):
                    resp = make_response(redirect("/"))
            
                    session['username'] = nombre
                    session['password'] = password
            
                    return resp
                else:
                    return render_template("index.html")
        else:
            return render_template("registro.html")
    else:
        return render_template("registro.html")

@app.route("/compr_usuario/<name>")
def comprobar_usuario(name):
    if Users.getUserFromDB(name) == None:
        return "<p class='bien'>El nombre de usuario esta disponible<p>"
    else:
        return "<p class='mal'>El nombre de usuario NO esta disponible<p>"




@app.route("/search", methods=['POST','GET'])
def search():
    json_url = os.path.join(SITE_ROOT, "data", "catalogo.json")
    pelis=jsonAPelicula(json_url)
    if request.method == 'GET':
        search=request.args.get('search')
        tipo=request.args.get('programa')

        return checkSessionPelis("last.html",peliculas=resultadoPeliculas(search,tipo,pelis), search=True)
    elif request.method == 'POST':
        search=request.form['search']
        tipo=request.form['programa']

        return checkSessionPelis("last.html",peliculas=resultadoPeliculas(search,tipo,pelis), search=True)
    else:
        return redirect(url_forurl_for('/'))

@app.route("/close")
def closeSession():

    if "SessionCookie" in request.cookies:

        session.clear()

    return redirect("/")


@app.route("/ajax_url", methods=['POST'])
def ajax():

    # PODRIA DAR ALGUN PROBLEMA DE PERDIDA DE DATOS (fork en so)
    # QUE SE REALICE UNA PETICION DEL MISMO USUARIO ANTES DE ACABAR DE EJECUTAR LA FUNCION ANTERIOR?
    
    if "basket" in session: 
        parse = json.loads(session['basket'])
        #print >>sys.stderr, 'READ: ' + str(parse)
    
    else: parse = {'films':[]}
    
    name = request.form['name']
    type = request.form['type']
    
    try:
        film = (item for item in parse['films'] if item["name"] == name).next()

        if type == "remove":
            parse['films'].remove(film)
            
        if type == "number":
            
            parse['films'].remove(film)
            
            number = request.form['number']
            old = film["number"]

            film["number"] = number
            
            parse['films'].append(film)
            
            session['basket'] = json.dumps(parse)
            
            return old
        
    except:
    
        if type == "add":
            parse['films'].append({'name':name, 'number':'1'})

    #print >>sys.stderr, 'WRITE: ' + str(parse)
    
    session['basket'] = json.dumps(parse)
    
    return "OK"
    
    
@app.route("/balance_ajax", methods=['POST'])
def balance_ajax():

    if "SessionCookie" in request.cookies:
    
        if 'username' in session and 'password' in session:

            if Users.checkUser(session['username'], session['password']):
            
                user = Users.getUserFromDB(session['username'])
            
                if not (user is None):
                
                    balance = request.form['balance']

                    if float(user.balance) < float(balance):
                        
                        user.balance = balance
                        
                        Users.updateUser(user)
                
                        return "OK"

    return "ERROR"
    
@app.route("/conected_users_ajax", methods=['POST'])
def conected_users_ajax():

    return str(random.randint(0,100))

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
    
        if 'username' in session and 'password' in session:

            if Users.checkUser(session['username'], session['password']):
                return render_template(url, user=session['username'])
                
    return redirect("/")


def checkSessionPelis(url, peliculas,search):
    ret={}
    dict_aux={}
    if "SessionCookie" in request.cookies:
        if "basket" in session:
        
            obj = json.loads(session['basket'])
                            
            buscar = obj["films"]

            dict_aux = peliculaEnCarrito(buscar)
            for resultado in peliculas:
                for peli,value in dict_aux.items():
                    if peli.titulo == resultado.titulo:
                        ret[peli]=value
    
        if 'username' in session and 'password' in session:

            if Users.checkUser(session['username'], session['password']):
                if len(ret) != 0:  
                    if search == False:
                        return render_template(url, dict_peliculas=ret, user=session['username'])
                    
                    else:
                        return render_template(url, dict_peliculas=ret, user=session['username'], search=True)
                else:
                    if search == False:
                        return render_template(url, peliculas=peliculas, user=session['username'])
                    else:
                        return render_template(url, peliculas=peliculas, user=session['username'], search=True)
    if len(ret) != 0:            
        if search == False:
            return render_template(url,dict_peliculas=ret)
        
        else:
            return render_template(url,dict_peliculas=ret,    search=True)
    else:
        if search == False:
            return render_template(url,peliculas=peliculas)
        
        else:
            return render_template(url, peliculas=peliculas,    search=True)


if __name__ == "__main__":
    app.run()

