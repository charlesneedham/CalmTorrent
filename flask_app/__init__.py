from flask import Flask, blueprints
import os

from .routes.rss import bp as rss_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(rss_bp)
    

    return app

