from flask import Blueprint, render_template, request, redirect, url_for
from services import product_service
from routes.auth_routes import login_requerido

product_bp = Blueprint('products', __name__)

@product_bp.route('/index')
def index():
    if not login_requerido(): return redirect(url_for('auth.login'))
    return render_template('index.html')

@product_bp.route('/productos')
def productos():
    items = product_service.listar_productos()
    return render_template('products.html', productos=items)

@product_bp.route('/crear', methods=['GET', 'POST'])
@product_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def formulario_producto(id=None):
    if not login_requerido(): return redirect(url_for('auth.login'))
    
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
    if not login_requerido(): return redirect(url_for('auth.login'))
    product_service.eliminar_producto(id)
    return redirect(url_for('products.index'))

# Las rutas de autenticación (login/logout) están en routes/auth_routes.py