import flask
from flask import request
from app.models.AuthModel import authmodel
app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/train', methods=['GET'])
def firstcall():
     intents = authmodel.getIntents()
     entity = authmodel.getEntity()
     print("intents", intents, entity)

if __name__ == "__main__":
    app.run()