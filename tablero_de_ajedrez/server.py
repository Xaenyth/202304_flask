from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def tablero_8x8():
    return render_template('tablero.html', filas=8, columnas=8)

@app.route('/<int:columnas>')
def tablero_parcial(columnas):
    return render_template('tablero.html', filas=8, columnas=columnas)

@app.route('/<int:filas>/<int:columnas>')
def tablero_personalizado(filas, columnas):
    return render_template('tablero.html', filas=filas, columnas=columnas)

if __name__ == '__main__':
    app.run()