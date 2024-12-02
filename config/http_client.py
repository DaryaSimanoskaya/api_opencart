import requests
import logging

from api.api_cart import ApiCart
from api.api_currency import ApiCurrency
from api.api_order import ApiOrder
from api.api_payment import ApiPayment

logger = logging.getLogger(__name__)

class HttpClient:
    def __init__(self, base_url, username, key):

        self.base_url = base_url
        self.session = requests.Session()
        params = {'username': username,
                  'key': key}
        response = requests.post(f"{self.base_url}api/account/login", data=params)
        json_response = response.json()
        print("Ответ от сервера:", json_response)
        logger.debug(f"Ответ JSON: {json_response}")  # Печать полного ответа
        token = json_response['api_token']
        self.session.params = {'api_token': token}

    @property
    def currency_api(self) -> callable:
        return ApiCurrency(self)

    @property
    def cart_api(self) -> callable:
        return ApiCart(self)

    @property
    def order_api(self) -> callable:
        return ApiOrder(self)

    @property
    def payment_api(self) -> callable:
        return ApiPayment(self)
