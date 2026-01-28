from flask import Flask, render_template, request, redirect, url_for
import db

app = Flask(__name__)

db.crear_tabla()


@app.route('/')
def root():
    return redirect(url_for('login'))


@app.route('/index')
def index():
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
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']

        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO productos (nombre, precio) VALUES (?, ?)",
            (nombre, precio)
        )
        conn.commit()
        conn.close()

        return redirect(url_for('index'))

    return render_template('form.html')


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    conn = db.get_connection()
    cursor = conn.cursor()

    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']

        cursor.execute(
            "UPDATE productos SET nombre=?, precio=? WHERE id=?",
            (nombre, precio, id)
        )
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    cursor.execute("SELECT * FROM productos WHERE id=?", (id,))
    producto = cursor.fetchone()
    conn.close()
    return render_template('form.html', producto=producto)


@app.route('/eliminar/<int:id>')
def eliminar(id):
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))


@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        precio = request.form['precio']

        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO productos (nombre, precio) VALUES (?, ?)",
            (nombre, precio)
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
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Credenciales inválidas')
    return render_template('login.html')
        

if __name__ == '__main__':
    app.run(debug=True)
