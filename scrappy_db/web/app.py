from flask import Flask
from scrappy_db.web.routes import main as main_blueprint
from scrappy_db.web.errors import register_error_handlers


def create_app():
    app = Flask(__name__)

    app.register_blueprint(main_blueprint)
    register_error_handlers(app)

    return app


def run():
    scrappy_app = create_app()
    scrappy_app.run(debug=False, host='0.0.0.0', port=9000)
