from app.utils.server import Server
from json import loads
from time import sleep

import os
import subprocess
import threading

RUNNING_PHONES = {}

class Emulator:
    
    def __init__(self,config,name) -> None:
        self.config = config
        self.name = name
        
    def getConfig(self):
        filename = self.config.Vms + f"\\{self.name}\\configs\\vm_config.json"
        if not os.path.exists(filename) or self.name == "MuMuPlayer-12.0-base" or self.name == "MuMuPlayer-12.0-0":
            return None
        return loads(open(filename,"r").read())
    
    def start(self):
        course = subprocess.Popen(
            [
                self.config.MuMuPlayer,
                '-v',
                self.name.replace("MuMuPlayer-12.0-", "")
            ]
        )
        config = self.getConfig()
        address = "127.0.0.1:" + \
            config["vm"]["nat"]["port_forward"]["adb"]["host_port"]
        threading.Thread(target=Server().connectAdb, args=(address,)).start()
        RUNNING_PHONES[self.name] = course
        return course
    
    def stop(self):
        if not RUNNING_PHONES.get(self.name):
            return True

        RUNNING_PHONES[self.name].kill()
        stdout = open("NUL", "w")
        subprocess.Popen(
            [
                self.config.MuMuVMMManage,
                'controlvm',
                self.name,
                'poweroff'
            ],
            stdout=stdout,
            stderr=stdout
        )
        stdout.close()
        RUNNING_PHONES[self.name] = None
        return True

    def restart(self):
        self.stop()
        self.start()
        
    def reset(self):
        self.stop()
        
        filename = self.config.Vms + f"\\{self.name}\\data.vdi"
        if not os.path.exists(filename):
            return True
        
        try:
            os.remove(filename)
        except:
            sleep(2)
            self.reset()
            
        return True