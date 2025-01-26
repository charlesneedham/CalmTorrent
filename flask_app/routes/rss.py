from flask import Blueprint, send_file, Flask
import os

app = Flask(__name__)
bp = Blueprint('rss', __name__)

@bp.route('/rss_feed')
def rss_feed():
    rss_file_path = os.path.join(os.path.dirname(__file__), '../../rss_xml/movies.xml')
    return send_file(rss_file_path, mimetype='application/rss+xml')