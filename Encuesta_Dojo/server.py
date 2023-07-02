from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('formulario.html')

@app.route('/process', methods=['POST'])
def process():
    nombre = request.form['nombre']
    localizacion = request.form['localizacion']
    lenguaje = request.form['lenguaje']
    comentario = request.form['comentario']

    return redirect(url_for('resultado', nombre=nombre, localizacion=localizacion, lenguaje=lenguaje, comentario=comentario))

@app.route('/resultado')
def resultado():
    nombre = request.args.get('nombre')
    localizacion = request.args.get('localizacion')
    lenguaje = request.args.get('lenguaje')
    comentario = request.args.get('comentario')

    return render_template('resultado.html', nombre=nombre, localizacion=localizacion, lenguaje=lenguaje, comentario=comentario)

if __name__ == '__main__':
    app.run(debug=True)