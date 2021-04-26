from os.path import dirname
import logging
import logging.config
import yaml
from os.path import dirname

with open(dirname(__file__) + '/log.yml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)
log = logging.getLogger(__name__)



YAML=dict()
with open(dirname(__file__) + "/config.yml") as file:
    YAML = yaml.load(file, Loader=yaml.FullLoader)



class RobinHood:
    def __init__(self, YAML):
        self.__authcode = YAML['RobinHood']['authcode']
        self.__user = YAML['RobinHood']['user']
        self.__password = YAML['RobinHood']['password']

    @property
    def authcode(self):
        return self.__authcode
    @property
    def user(self):
        return self.__user
    @property
    def password(self):
        return self.__password


class Config:
    def __init__(self, YAML):
        self.rh = RobinHood(YAML)

    @property
    def RobinHood(self):
        return self.rh  

    @property
    def parent_id(self):
        return self.YAML['parent_id']

try:
    CONFIG=Config(YAML)
except Exception as e:
    log.error(e)
