
from modules.task_action import *
from modules.task_check import *

conditions = {

    'battery': {
        'check': checkBattery,
        'action': sendBattery
    },
    

}
