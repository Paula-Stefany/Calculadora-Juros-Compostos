from flask import Flask, render_template


app = Flask(__name__)

@app.route('/Calculadora')
def calculadora():
    return render_template('calculadora.html')
