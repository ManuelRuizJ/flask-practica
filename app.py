from flask import Flask, render_template, request, redirect, url_for, session
import db

app = Flask(__name__)
app.secret_key = "clave_secreta"


db.crear_tabla()
# db.agregar_categoria()


def login_requerido():
    return 'user' in session



@app.route('/')
def root():
    return redirect(url_for('login'))


@app.route('/index')
def index():
    if not login_requerido():
        return redirect(url_for('login'))
    return render_template('index.html')


@app.route('/productos')
def productos():
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conn.close()
    return render_template('products.html', productos=productos)


@app.route('/crear', methods=['GET', 'POST'])
def crear():
    if not login_requerido():
        return redirect(url_for('login'))
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        stock = int(request.form['stock'])
        activo = 1 if request.form.get('activo') else 0
        categoria = request.form['categoria']
        conn = db.get_connection()
        cursor = conn.cursor()

        if nombre == '' or precio < 0 or stock < 0:
            return "Datos inválidos", 400
        cursor.execute(
            "INSERT INTO productos (nombre, precio, stock, activo, categoria) VALUES (?, ?, ?, ?, ?)",
            (nombre, precio, stock, activo, categoria)
        )
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    return render_template('form.html')


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if not login_requerido():
        return redirect(url_for('login'))
    conn = db.get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        stock = int(request.form['stock'])
        activo = 1 if request.form.get('activo') else 0
        categoria = request.form['categoria']

        cursor.execute(
            "UPDATE productos SET nombre=?, precio=?, stock=?, activo=?, categoria=? WHERE id=?",
            (nombre, precio, stock, activo, categoria, id)
        )

        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    cursor.execute("SELECT * FROM productos WHERE id=?", (id,))
    producto = cursor.fetchone()
    conn.close()
    return render_template('form.html', producto=producto)


@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    if not login_requerido():
        return redirect(url_for('login'))

    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))



@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if not login_requerido():
        return redirect(url_for('login'))
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = float(request.form['precio'])
        stock = int(request.form['stock'])
        activo = 1 if request.form.get('activo') else 0
        categoria = request.form['categoria']
        conn = db.get_connection()
        cursor = conn.cursor()

        if nombre == '' or precio < 0 or stock < 0:
            return "Datos inválidos", 400
        cursor.execute(
            "INSERT INTO productos (nombre, precio, stock, activo, categoria) VALUES (?, ?, ?, ?, ?)",
            (nombre, precio, stock, activo, categoria)
        )
        conn.commit()
        conn.close()

        return redirect(url_for('productos'))

    return render_template('form.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        if username == 'admin' and password == 'admin':
            session['user'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Credenciales inválidas')

    return render_template('login.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

        

if __name__ == '__main__':
    app.run(debug=True)
