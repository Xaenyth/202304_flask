from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "mi_clave_secreta"

@app.route('/')
def contador():
    if 'contador' not in session:
        session['contador'] = 0
    
    session['contador'] += 1
    
    return render_template('contador.html', contador=session['contador'])

@app.route('/increment')
def increment():
    session['contador'] += 1
    return redirect(url_for('contador'))

@app.route('/reset')
def reset():
    session['contador'] = 0
    return redirect(url_for('contador'))

if __name__ == '__main__':
    app.run()