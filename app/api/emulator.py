from sanic.blueprints import Blueprint
from app.utils.response import response
from app.utils.emulator import Emulator as _Emulator

emulator = Blueprint(name="emulator", url_prefix="/emulator")


@emulator.route("/info", ["POST"])
async def getInfo(request):
    config = _Emulator(request.app.config,request.json["name"]).getConfig()
    
    if not config:
        return response.error("模拟器不存在")
    
    return response.succWithData(config)

@emulator.route("/operate/<action>", ["POST"])
async def operate(request,action):
    config = _Emulator(request.app.config,request.json["name"]).getConfig()
    
    if not config:
        return response.error("模拟器不存在")
    
    control = _Emulator(request.app.config,request.json["name"])
    

    if action not in ("start", "stop", "reset","restart"):
        return response.error("操作不受支持")
    
    getattr(control, action)()
    
    return response.success()