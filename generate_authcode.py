#!/usr/bin/env python3
from chalicelib.config import CONFIG
from chalicelib.RobinHood import robin_hood_authcode

print( robin_hood_authcode(CONFIG) )
print("Hello!")
