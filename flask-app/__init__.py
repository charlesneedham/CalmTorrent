from flask import Flask, render_template, redirect, url_for, request, send_from_directory
import os


def create_app():
    app = Flask(__name__)
    
    @app.route('/rss_feed')

    def rss_feed():
        rss_directory = os.path.join(app.root_path, 'rss_xml')
        return send_from_directory(rss_directory, 'feed.xml')

    return app

