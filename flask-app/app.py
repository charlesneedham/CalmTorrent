from flask import Flask, render_template, redirect, url_for, request, send_from_directory
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    


    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    class User(UserMixin):
        def __init__(self, id):
            self.id = id

    users = {'user': {'password': 'password'}}

    @login_manager.user_loader
    def load_user(user_id):
        return User(user_id)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            if username in users and users[username]['password'] == password:
                user = User(username)
                login_user(user)
                return redirect(url_for('rss_feed'))
        return render_template('login.html')

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('login'))

    @app.route('/rss_feed')
    @login_required
    def rss_feed():
        rss_directory = os.path.join(app.root_path, 'rss_xml')
        return send_from_directory(rss_directory, 'feed.xml')

    return app

