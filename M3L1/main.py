from flask import Flask
import random
app = Flask(__name__)
facts_list = [
    "La primera computadora electrónica, ENIAC, fue construida en 1945 y ocupaba una habitación entera.",
    "La gran muralla china es la estructura más larga jamás construida por el ser humano, con una longitud de aproximadamente 21,196 kilómetros.",
    "Yo (el original)",
    "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos",
    "Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo"
]



@app.route("/")
def home():
    return """<h1>Esta es la mejor pagina del mundo :)</h1>
    
    <a href="/fact">Click aqui para ver datos curiosos</a>"""

@app.route("/fact")
def hello_world():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/secret")
def secreto():
    return """<h1>Como llegaste aqui? :O Eres un haker</h1>
    <p>Pagina hecha por yo(el original)</p>
    <a href="/">Click aqui para volver a la pagina principal</a>
    <p>Si quieres pasar el rato, tenes un juego de cara o cruz</p>
    <a href="/jk">Click aqui para jugar cara o cruz</a>
    """

@app.route("/jk")
def broma():
    return "<h1>Era mentira :P</h1>"
app.run(debug=True)

