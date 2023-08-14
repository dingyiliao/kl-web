from flask import (Flask,
                   render_template,
                   request)
from sqlalchemy import MetaData

from Backend.extensions import (db, 
                                whooshee)
from Backend.services import services_blueprint
from Backend.utils import register_view
from Backend.views import views_blueprint


def create_app(config=None):
    app = Flask(__name__, 
                static_folder='static',
                template_folder='templates')

    configure_app(app, config)
    configure_before_handlers(app)
    configure_errorhandlers(app)
    configure_extensions(app)
    configure_blueprints(app)

    # prepare for db
    with app.app_context():
        db.create_all()

    return app


def configure_app(app, config):
    if isinstance(config, str):
        app.config.from_pyfile(config)
    else:
        app.config.from_object(config)


def configure_before_handlers(app):
    
    @app.before_request
    def handler():
        req = request
        return


def configure_errorhandlers(app):

    @app.errorhandler(403)
    def forbidden_page(error):
        return render_template('errors/forbidden_page.html'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/page_not_found.html'), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template('errors/server_error.html'), 500


def configure_extensions(app):
    db.init_app(app)
    whooshee.init_app(app)


def configure_blueprints(app):
    app.register_blueprint(views_blueprint)
    app.register_blueprint(services_blueprint, url_prefix='/api/v1')
