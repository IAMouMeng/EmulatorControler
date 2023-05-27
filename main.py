from json import loads
from sanic import Sanic
from app.api import *

app = Sanic(__name__)

app.config.update(loads(open("./config.json","r",encoding="utf-8").read()))
app.blueprint(api)

if __name__ == '__main__':
    app.run(host="localhost", port=7800, debug=True, auto_reload=True)