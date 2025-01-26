from flask import send_from_directory, Blueprint, Flask
import os

app = Flask(__name__)
bp = Blueprint('rss', __name__)


@bp.route('/rss_feed', methods=['GET'])
def rss_feed():
    rss_directory = os.path.join(app.root_path, 'rss_xml')
    return send_from_directory(rss_directory, 'movies.xml')