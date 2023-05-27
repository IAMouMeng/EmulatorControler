from sanic.response import json
from time import time

class response:
    
    def response(code,msg,data=None):
        return json({"code":code,"msg":msg,"timestmp":int(round(time() * 1000)),"data":data})
    
    def error(msg="error"):
        return response.response(code=400,msg=msg)
    
    def success(msg="success"):
        return response.response(code=200,msg=msg)
    
    def succWithData(data=None,msg="success"):
        return response.response(code=200,msg=msg,data=data)
    