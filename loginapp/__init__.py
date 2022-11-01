from flask import Flask

from .extensions import mongo

from .main.routes import main

def create_app():

    app = Flask(__name__)

    app.config['MONGO_URI'] = 'mongodb+srv://mydb:nf12sLAqHwXDJvDb@cluster0.0t9uvua.mongodb.net/mydb?retryWrites=true&w=majority'
    
    mongo.init_app(app)

    app.register_blueprint(main)

    return app
