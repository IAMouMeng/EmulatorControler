from .emulator import emulator
from .server import server
from sanic.blueprints import Blueprint

blueprints = [
    emulator,
    server
]

api = Blueprint.group(*blueprints, url_prefix="/api")
