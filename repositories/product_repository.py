import db

def get_all_products():
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conn.close()
    return productos

def get_product_by_id(id):
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos WHERE id=?", (id,))
    producto = cursor.fetchone()
    conn.close()
    return producto

def insert_product(nombre, precio, stock, activo, categoria):
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO productos (nombre, precio, stock, activo, categoria) VALUES (?, ?, ?, ?, ?)",
        (nombre, precio, stock, activo, categoria)
    )
    conn.commit()
    conn.close()

def update_product(id, nombre, precio, stock, activo, categoria):
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE productos SET nombre=?, precio=?, stock=?, activo=?, categoria=? WHERE id=?",
        (nombre, precio, stock, activo, categoria, id)
    )
    conn.commit()
    conn.close()

def delete_product(id):
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id=?", (id,))
    conn.commit()
    conn.close()