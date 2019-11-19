# coding=utf-8
"""
author = jamon
"""

from flask import Blueprint, Flask, request, Response


flask_login_blueprint = Blueprint("flask", __name__, url_prefix="/flask")

flask_login_blueprint = Blueprint("flask", __name__, url_prefix="/flask")

@flask_login_blueprint.route("/login", methods=["POST"])
def login():
    if request.method != "POST":
        return Response("test")
    tt = request.form.get("phone")
    return

@flask_login_blueprint.route("/login", methods=["POST"])
def login():
    if request.method != "POST":
        return Response("flask method error!")

    phone = request.form.get("phone")
    print("flask_login phone=", phone)
    return Response("flask handler ok")


if __name__ == "__main__":
    app = Flask(__name__)
    app = Flask(__name__)
    app.register_blueprint(flask_login_blueprint)
    app.run("0.0.0.0", port=8888)