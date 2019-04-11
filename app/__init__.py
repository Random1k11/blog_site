from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap
from posts.blueprint import posts
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
app.register_blueprint(posts, url_prefix='/blog')
migrate = Migrate(app, db)


from app import routes
app.config.from_object(Config)
