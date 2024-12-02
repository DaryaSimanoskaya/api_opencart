class ApiPayment:
    def __init__(self, client):
        self.client = client

    def post_payment_address(self,
                             firstname: str,
                             lastname: str,
                             address_1: str,
                             city: str,
                             country_id: str,
                             zone_id: int):
        data = {
            'firstname': firstname,
            'lastname': lastname,
            'address_1': address_1,
            'city': city,
            'country_id': country_id,
            'zone_id': zone_id
        }
        response = self.client.session.post(f"{self.client.base_url}api/sale/payment_address",
                                            data=data)
        return response
