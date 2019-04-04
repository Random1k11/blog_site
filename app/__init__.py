from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)


from app import routes
app.config.from_object(Config)
