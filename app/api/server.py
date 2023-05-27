import psutil
import platform
from sanic.blueprints import Blueprint
from app.utils.response import response
from app.utils.server import Server as _Server
from app.utils.emulator import Emulator

server = Blueprint(name="server", url_prefix="/server")

@server.route("/list", ["GET"])
async def getRunningList(request):
    
    Host = _Server(request.app.config)
    AllEmulater = Host.getAllEmulater()
    RunningEmulater = Host.getRunningEmulater()
    
    result = []
    
    for a in AllEmulater:
        if a in RunningEmulater:
            result.append({"name":a,"status":"online"})
        else:
            result.append({"name":a,"status":"offline","info":Emulator(request.app.config,a).getConfig()})
            
    return response.succWithData(result)

@server.route("/info", ["GET"])
async def getServerInfo(request):
    data = {
        "system":platform.system(),
        "machine": platform.machine(),
        "host":platform.node(),
    }
    return response.succWithData(data)


@server.route("/rate", ["GET"])
async def getUseRate(request):
    memoryInfo = psutil.virtual_memory()
    diskInfo = psutil.disk_usage("C://")
    netInfo = psutil.net_io_counters()
    data = {
        "cpu":{
            "total":psutil.cpu_count(logical=False),
            "used":psutil.cpu_percent(interval=0.5)
        },
        "memory":{
            "total":round(memoryInfo.total/1024/1024/1024,2),
            "used":memoryInfo.percent,
        },
        "disk":{
            "total":round(diskInfo.total/1024/1024/1024,2),
            "used":diskInfo.percent,
        },
        "net":{
            "send":netInfo.bytes_sent,
            "receive":netInfo.bytes_recv
        }
    }
            
    return response.succWithData(data)