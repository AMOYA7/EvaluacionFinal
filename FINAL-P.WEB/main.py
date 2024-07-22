from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        # Procesar los datos del formulario del ejercicio 1
        return redirect(url_for('resultado_ejercicio1'))
    return render_template('ejercicio1.html')

@app.route('/resultado_ejercicio1')
def resultado_ejercicio1():
    # Renderizar la plantilla de resultado del ejercicio 1
    return render_template('resultado_ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        # Procesar los datos del formulario del ejercicio 2
        return redirect(url_for('resultado_ejercicio2'))
    return render_template('ejercicio2.html')

@app.route('/resultado_ejercicio2')
def resultado_ejercicio2():
    # Renderizar la plantilla de resultado del ejercicio 2
    return render_template('resultado_ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)