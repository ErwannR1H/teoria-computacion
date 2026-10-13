from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index.html')
def home():
    # Flask cherche par défaut dans un dossier nommé "templates"
    return render_template('index.html')

@app.route("/")
def hola_mundo():
    return "Hola Mundo con Flask"

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run()
