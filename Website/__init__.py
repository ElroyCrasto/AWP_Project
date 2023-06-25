# Imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_cors import CORS

# Creeting SQLALchemy Database Object
Database = SQLAlchemy()


def CreateApp():
    # App Configuration
    App = Flask(__name__)
    App.config["SECRET_KEY"] = " "

    # Database Configuration
    App.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Database.db"
    from .DatabaseModels import TestTable
    Database.init_app(App)

    # Blueprints
    from .DefaultRoutes import Default
    App.register_blueprint(Default)

    # API Configuration
    API = Api(App)
    from .APIResources import Test
    API.add_resource(Test, "/api/")
    CORS(App)

    # Special Route
    @App.before_request
    def SetupDatabase():
        Database.create_all()
        Database.session.commit()

    return App