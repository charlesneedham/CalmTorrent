from flask import send_from_directory, blueprints, Flask
import os

bp = blueprints('rss', __name__)

app = Flask(__name__)

@bp.route('/rss_feed')
def rss_feed():
    rss_directory = os.path.join(app.root_path, 'rss_xml')
    return send_from_directory(rss_directory, 'feed.xml')