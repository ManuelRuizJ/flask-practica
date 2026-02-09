from flask import Flask, redirect, url_for
from routes.product_routes import product_bp
from routes.auth_routes import auth_bp
import db

def create_app():
    app = Flask(__name__)
    app.secret_key = "s"

    # 1. Inicializar DB
    db.crear_tabla()

    # 2. Registrar Blueprints
    app.register_blueprint(product_bp)
    app.register_blueprint(auth_bp)

    @app.route('/')
    def home():
        return redirect(url_for('auth.login'))

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)