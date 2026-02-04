from repositories import product_repository

def listar_productos():
    return product_repository.get_all_products()

def obtener_producto(id):
    return product_repository.get_product_by_id(id)

def guardar_producto(datos, id=None):
    nombre = datos.get('nombre')
    precio = float(datos.get('precio', 0))
    stock = int(datos.get('stock', 0))
    activo = 1 if datos.get('activo') else 0
    categoria = datos.get('categoria')

    # Validaciones
    if not nombre or precio < 0 or stock < 0:
        return False, "Datos inválidos"

    if id:
        product_repository.update_product(id, nombre, precio, stock, activo, categoria)
    else:
        product_repository.insert_product(nombre, precio, stock, activo, categoria)
    
    return True, "Operación exitosa"

def eliminar_producto(id):
    product_repository.delete_product(id)