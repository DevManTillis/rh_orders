from inspect import Parameter
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

if YAML['settings']['env'].lower() == "development":
    with open(YAML['settings']['dev_config_path']) as file:
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

class CoinMarketCap:
    def __init__(self, YAML):
        pass
    parameters = YAML['CoinMarketCap']['parameters']
    url = YAML['CoinMarketCap']['url']
    api_key = YAML['CoinMarketCap']['api_key']

class BinanceUS:
    def __init__(self, YAML):
        pass
    parameters = YAML['BinanceUS']['parameters']
    url = YAML['BinanceUS']['url']
    api_key = YAML['BinanceUS']['api_key']
    secret_key = YAML['BinanceUS']['secret_key']

class Config:
    def __init__(self, YAML):
        pass
    RobinHood = RobinHood(YAML)
    AWS       = AWS(YAML)
    CoinMarketCap = CoinMarketCap(YAML)
    BinanceUS = BinanceUS(YAML)


try:
    CONFIG=Config(YAML=YAML)
except Exception as e:
    log.error(e)
