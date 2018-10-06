from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/last")
def last():
    return render_template("last.html")

@app.route("/fullFilm")
def fullFilm():
    return render_template("fullFilm.html")

@app.route("/basket")
def basket():
    return render_template("basket.html")

@app.route("/history")
def history():
    return render_template("history.html")

@app.route("/sing_up")
def registro():
    return render_template("registro.html")

@app.route("/search")
def search():
    return render_template("search.html")



@app.route('/images/<path:path>')
def send_js(path):
    return send_from_directory('static/images', path)

@app.route('/styles/<path:path>')
def send_styles(path):
    return send_from_directory('templates/styles', path)

if __name__ == "__main__":
    app.run()

