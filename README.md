# RobinHood Orders AWS Lambda App
Use this app in order to integrate robin hood crypto and stock trade orders with essentially any application.
Deploy in AWS lambda in order to make requests of HTTP to initiate trades.

### Quick Start
This software is provided as is. No warranty. Can not be used without written consent from the developer. This is closed source software.

## Add config/config.yml configuration
```yaml
RobinHood:
  authcode: "Your robinhood account two factor code"
  user: "your robin hood user name"
  password: "your password"
AWS:
  access_key_id: ""
  secret_access_key: ""
CoinMarketCap:
  url: "https://sandbox-api.coinmarketcap.com/v1/"
  api_key: ""
  parameters:
    start: "1"
    limit: "5000"
    convert: "USD"
```

## Setup ENV
```bash
python3 -m pip install virtualenv
virtualenv venv
. venv/bin/activate
python3 -m pip install -r lib/requirements.txt
```

## Run
```bash
./run.sh
```

## Setup AWS-CLI authentication
```bash
aws configure
aws configure --profile "RDSCreds"
```

## Setup AWS Chalice
```bash
chalice new-project chalice-proj-dev
```

## Test Locally on your laptop
```bash
chalice local --port=8000
```

## Deploy App to AWS Lambda
```bash
chalice deploy
```

## Request Format Crypto
```json
{"ticker": "LTCUSD", "equity_type": "crypto", "price": 2007.53, "time": "2021-03-13T22", "order_type": "stop_loss"}
```

## Request Format Stock
```json
{"ticker": "SI", "equity_type": "stock", "price": 2007.53, "time": "2021-03-13T22", "order_type": "stop_loss"}
```

## Manually Test
- Build & test on Ubuntu18.04
- Use Insomnia Client to test local and remote POST events
- Create AWS user API key for shell use
- Modify In AWS Lambda UI line 82 of robin_stocks/authentication.py  home_dir = os.path.expanduser("~") --> home_dir = os.path.expanduser("/tmp")
- View AWS lambda logs, click lambda function, click monitor tab, click view logs in cloudwatch

Tasks
- [x] Capability to buy crypto
- [x] Capability to sell crypto (market order)
- [x] Capability to cancel all orders
- [x] Capability to do all of the above at a price that is at or below a target


# robin-stocks module docs
- https://pypi.org/project/robin-stocks/
- http://www.robin-stocks.com/en/latest/functions.html
- http://www.robin-stocks.com/en/latest/robinhood.html

# chalice docs
- https://chalice-workshop.readthedocs.io/en/latest/env-setup.html#setting-up-aws-credentials
