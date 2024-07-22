from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])

        total_sin_descuento = tarros * 9000


        if edad >= 18 and edad <= 30:
            descuento_aplicado = total_sin_descuento * 0.15
        elif edad > 30:
            descuento_aplicado = total_sin_descuento * 0.25
        else:
            descuento_aplicado = 0

        total_a_pagar = total_sin_descuento - descuento_aplicado

        return render_template('resultado_ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento,
                               descuento_aplicado=descuento_aplicado, total_a_pagar=total_a_pagar)

    return render_template('ejercicio1.html')


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']


        if usuario == 'juan' and contraseña == 'admin':
            mensaje = 'Bienvenido administrador Juan'
        elif usuario == 'pepe' and contraseña == 'user':
            mensaje = 'Bienvenido usuario Pepe'
        else:
            mensaje = 'Usuario o contraseña incorrectos'


        return render_template('resultado_ejercicio2.html', mensaje=mensaje)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)