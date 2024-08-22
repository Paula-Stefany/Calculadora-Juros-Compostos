from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/Calculadora', methods=['GET', 'POST'])
def calculadora():

    if request.method == 'POST':
        value = float(request.form['initial-value'])
        fees = float(request.form['compound-interest'])
        months = int(request.form['months'])

        result = value * ((1 + (fees/100)) ** months)
        result = round(result, 2)

        return render_template('calculadora.html', result=result)

    return render_template('calculadora.html')

if __name__ == '__main__':
    app.run(debug=True)
