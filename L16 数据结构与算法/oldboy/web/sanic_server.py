# coding=utf-8
"""
author = jamon
"""

from sanic import Sanic
from sanic.response import text

app = Sanic()


@app.route("/sanic/login", methods=["POST"])
async def login(request):
    return text("sanic login success")


if __name__ == "__main__":
    app.run("0.0.0.0", port=8888)

