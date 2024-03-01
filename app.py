from flask import Flask 
from flask_migrate import Migrate
from models import db
from girls_views.girl_1.views import girl1_bp
from girls_views.girl_2.views import girl2_bp


app = Flask(__name__)

app.config.from_object("config.Config")

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(girl1_bp)
app.register_blueprint(girl2_bp)


from views import *

if __name__ == "__main__":
    app.run()
