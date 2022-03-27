from os.path import dirname
import logging
import logging.config
import yaml
from os.path import dirname

with open(dirname(__file__) + '/log.yml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

YAML=dict()
with open(dirname(__file__) + "/config.yml") as file:
    YAML = yaml.load(file, Loader=yaml.FullLoader)

if YAML['RobinHood']['env'].lower() == "development":
    with open(YAML['RobinHood']['dev_config_path']) as file:
        YAML = yaml.load(file, Loader=yaml.FullLoader)

log = logging.getLogger(__name__)

class RobinHood:
    def __init__(self, YAML):
        pass
    authcode = YAML['RobinHood']['authcode']
    user     = YAML['RobinHood']['user']
    password = YAML['RobinHood']['password']


class AwsLambda:
    def __init__(self, YAML):
        pass
    __aws = YAML['AWS']
    access_key_id     = __aws['access_key_id']
    secret_access_key = __aws['secret_access_key']


class AWS:
    def __init__(self, YAML):
        pass
    aws_lambda = AwsLambda(YAML)


class Config:
    def __init__(self, YAML):
        pass
    rh        = RobinHood(YAML)
    RobinHood = RobinHood(YAML)
    authcode  = rh.authcode
    user      = rh.user
    password  = rh.password
    AWS       = AWS(YAML)


try:
    CONFIG=Config(YAML=YAML)
except Exception as e:
    log.error(e)
