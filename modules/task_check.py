import os
import json
# ipconfig
# termux-battery-status
def checkBattery() -> None:
    cmd = os.popen('termux-battery-status')
    try:
        cmd_str = json.loads(cmd.read())
    except:
        cmd_str = '{}'
    print(cmd_str)
    
    return True
