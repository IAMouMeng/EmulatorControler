import subprocess
from time import sleep
import os


class Server:
    
    def __init__(self,config = None) -> None:
        self.config = config
        
    def getAllEmulater(self):
        result = []
        for name in os.listdir(self.config.Vms):
            if name == "MuMuPlayer-12.0-base" or name == "MuMuPlayer-12.0-0":
                continue
            result.append(name)
        return result

    def getRunningEmulater(self):
        task = subprocess.Popen(
            [
                self.config.MuMuVMMManage,
                'list',
                'runningvms'
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        task.wait()
        data = []
        stdout = task.stdout.read().decode("utf-8").replace('"', "").split("\r\n")
        for name in stdout:
            if name:
                data.append(name.split(" ")[0])
        return data
    
    def connectAdb(self,address):
        for _ in range(30):
            task = subprocess.Popen(
                [
                    "adb",
                    "connect",
                    address
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            task.wait()
            stdout = task.stdout.read().decode("utf-8")
            if "already connected" in stdout:
                return True
            sleep(1)
        return False
