from flask import Flask, render_template, send_from_directory, request, redirect, make_response
import datetime

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
                return "POST"

        else:
            return render_template("index.html")

@app.route("/last")
def last():
    return checkSession("last.html")

@app.route("/fullFilm")
def fullFilm():
    return checkSession("fullFilm.html")

@app.route("/basket")
def basket():
    return checkSession("basket.html")

@app.route("/history")
def history():
    return checkSession("history.html")

@app.route("/sing_up")
def registro():
    return checkSession("registro.html")

@app.route("/search", methods=['GET'])
def search():
    if request.method == 'GET':
        return "hola"
    else:
        return render_template("search.html")

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
def send_js(path):
    return send_from_directory('static/images', path)

@app.route('/styles/<path:path>')
def send_styles(path):
    return send_from_directory('templates/styles', path)



def checkSession(url):

    if "SessionCookie" in request.cookies:
        return render_template(url)
    else:
        return redirect("/")

if __name__ == "__main__":
    app.run()

