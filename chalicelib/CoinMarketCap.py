#!/usr/bin/env python3
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import inspect
from config import CONFIG, log


class RequestPrereqs:
    url = f'{CONFIG.CoinMarketCap.url}'
    parameters = CONFIG.CoinMarketCap.parameters
    headers = {
      'Accepts': 'application/json',
      'X-CMC_PRO_API_KEY': CONFIG.CoinMarketCap.api_key
    }
    session = Session()
    session.headers.update(headers)


class cmc_api(RequestPrereqs):
    def __init__(self) -> None:
        super().__init__()

    def request(self, endpoint) -> dict():
        self.url = self.url + endpoint
        try:
            response = self.session.get(self.url, params=self.parameters)
            data = json.loads(response.text)
            return data
        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
            return False


print(cmc_api().request(endpoint="cryptocurrency/listings/latest"))