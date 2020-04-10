import flask
from flask import request
from app.models.AuthModel import authmodel
flask1 = flask.Flask(__name__)
flask1.config["DEBUG"] = True

@flask1.route('/train', methods=['GET'])
def firstcall():
     user = authmodel.getUser()
    return render_template('index.html', title='Home', user=user)