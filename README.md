# Quick Start

## Add config/config.yml configuration
```yaml
RobinHood:
  authcode: "Your robinhood account two factor code"
  user: "your robin hood user name"
  password: "your password"
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

## Manually Test
- Build & test on Ubuntu18.04
- Use Insomnia Client to test local and remote POST events
- Modify In AWS Lambda UI line 82 of robin_stocks/authentication.py  home_dir = os.path.expanduser("~") --> home_dir = os.path.expanduser("/tmp")

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

# tutorial for building webhook trade app
- https://www.youtube.com/watch?v=TKAo_Z-hzQs
