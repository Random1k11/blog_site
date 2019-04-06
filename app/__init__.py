from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from posts.blueprint import posts



app = Flask(__name__)
bootstrap = Bootstrap(app)
app.register_blueprint(posts, url_prefix='/blog')


from app import routes
app.config.from_object(Config)
