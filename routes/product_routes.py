from flask import Blueprint, render_template, request, redirect, url_for, session
from services import product_service

product_bp = Blueprint('products', __name__)

def login_requerido():
    return 'user' in session

@product_bp.route('/index')
def index():
    if not login_requerido(): return redirect(url_for('products.login'))
    return render_template('index.html')

@product_bp.route('/productos')
def productos():
    items = product_service.listar_productos()
    return render_template('products.html', productos=items)

@product_bp.route('/crear', methods=['GET', 'POST'])
@product_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def formulario_producto(id=None):
    if not login_requerido(): return redirect(url_for('products.login'))
    
    producto = None
    if id:
        producto = product_service.obtener_producto(id)

    if request.method == 'POST':
        exito, mensaje = product_service.guardar_producto(request.form, id)
        if exito:
            return redirect(url_for('products.index'))
        return mensaje, 400

    return render_template('form.html', producto=producto)

@product_bp.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    if not login_requerido(): return redirect(url_for('products.login'))
    product_service.eliminar_producto(id)
    return redirect(url_for('products.index'))

@product_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('username') == 'admin' and request.form.get('password') == 'admin':
            session['user'] = 'admin'
            return redirect(url_for('products.index'))
        return render_template('login.html', error='Credenciales inválidas')
    return render_template('login.html')

@product_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('products.login'))