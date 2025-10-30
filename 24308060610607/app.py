from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def formulario():
    return render_template("formulario.html")

@app.route("/resultado")
def calculo():
    return render_template("resultado.html")

if __name__ == "__main__":
    app.run(debug=True)