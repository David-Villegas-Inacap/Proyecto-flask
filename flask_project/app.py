from flask import Flask, render_template, request, redirect, flash, url_for
from flask_sqlalchemy import SQLAlchemy
from config import Config
from models import db, Cliente, Transaccion
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

# Inicializar la base de datos
db.init_app(app)

# Página inicial con el menú
@app.route('/')
def index():
    return render_template('index.html')

# Formulario para agregar cliente
@app.route('/agregar-cliente', methods=['GET', 'POST'])
def agregar_cliente():
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            rut = request.form['rut']
            dv = request.form['dv']
            nombre = request.form['nombre']
            apellido_paterno = request.form['apellido_paterno']
            apellido_materno = request.form['apellido_materno']
            celular = request.form['celular']
            correo = request.form['correo']

            # Crear y guardar el cliente
            nuevo_cliente = Cliente(rut=rut, dv=dv, nombre=nombre, apellido_paterno=apellido_paterno,
                                    apellido_materno=apellido_materno, celular=celular, correo=correo)
            db.session.add(nuevo_cliente)
            db.session.commit()
            flash("Cliente agregado exitosamente", "success")
            return redirect(url_for('listar_clientes'))
        except Exception as e:
            flash(f"Error: {e}", "error")
    return render_template('agregar_cliente.html')

# Listar clientes
@app.route('/lista-clientes')
def listar_clientes():
    clientes = Cliente.query.all()
    return render_template('lista_clientes.html', clientes=clientes)

# Formulario para agregar transacción
@app.route('/agregar-transaccion', methods=['GET', 'POST'])
def agregar_transaccion():
    if request.method == 'POST':
        try:
            descripcion = request.form['descripcion']
            monto = float(request.form['monto'])
            fecha = datetime.strptime(request.form['fecha'], '%Y-%m-%d')
            categoria = request.form['categoria']

            nueva_transaccion = Transaccion(descripcion=descripcion, monto=monto, fecha=fecha, categoria=categoria)
            db.session.add(nueva_transaccion)
            db.session.commit()
            flash("Transacción agregada exitosamente", "success")
            return redirect(url_for('listar_transacciones'))
        except Exception as e:
            flash(f"Error: {e}", "error")
    return render_template('agregar_transaccion.html')

# Listar transacciones
@app.route('/mostrar-transacciones')
def listar_transacciones():
    transacciones = Transaccion.query.all()
    return render_template('lista_transacciones.html', transacciones=transacciones)

if __name__ == '__main__':
    app.run(debug=True)