#!/usr/bin/env python3
import urllib.parse
import hashlib
import hmac
import base64
import requests
import calendar
import time
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import inspect
from config import CONFIG, log


class RequestPrereqs:
    url = CONFIG.BinanceUS.url
    headers = {}
    headers['X-MBX-APIKEY'] = CONFIG.BinanceUS.api_key

    # get binanceus signature
    def get_binanceus_signature(self, data) -> str():
        postdata = urllib.parse.urlencode(data)
        message = postdata.encode()
        byte_key = bytes(CONFIG.BinanceUS.secret_key, 'UTF-8')
        mac = hmac.new(byte_key, message, hashlib.sha256).hexdigest()
        return mac


class bus_api(RequestPrereqs):
    def __init__(self) -> None:
        super().__init__()

    def request(self, uri_path, data) -> dict():
        signature = self.get_binanceus_signature(data) 
        payload={
            **data,
            "signature": signature,
            }           
        req = requests.post((CONFIG.BinanceUS.url + uri_path), headers=self.headers, data=payload)
        return req.text


data = {
    "symbol": "BTCUSDT",
    "side": "BUY",
    "type": "LIMIT",
    "timeInForce": "GTC",
    "quantity": 1,
    "price": 0.1,
    "timestamp": int(round(time.time() * 1000))
}

endpoint = "api/v3/order"
print(bus_api().request(endpoint, data))