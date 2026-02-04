import sqlite3
from flask import g

DATABASE = 'productos.db'

def get_connection():
    return sqlite3.connect(DATABASE)


def crear_tabla():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL CHECK (precio >= 0),
            stock INTEGER NOT NULL DEFAULT 0 CHECK (stock >= 0),
            activo BOOLEAN NOT NULL
        )
    """)

def agregar_categoria():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        ALTER TABLE productos
            ADD categoria TEXT DEFAULT NULL
    """)
    conn.commit()
    conn.close()
