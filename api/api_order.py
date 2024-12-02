class ApiOrder:
    def __init__(self, client):
        self.client = client

    def post_order_add(self):
        response = self.client.session.post(f"{self.client.base_url}api/sale/order.load")
        return response
