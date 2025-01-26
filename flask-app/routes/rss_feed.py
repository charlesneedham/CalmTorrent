from flask import Flask, send_from_directory, blueprints
import os

app = Flask(__name__)

bp = blueprints.Blueprint('rss_feed', __name__)


@bp.route('/rss')
def rss_feed():
    rss_directory = os.path.join(app.root_path, 'rss_xml')
    return send_from_directory(rss_directory, 'feed.xml')

if __name__ == '__main__':
    app.run(debug=True)
