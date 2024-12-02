class ApiCart:
    def __init__(self, client):
        self.client = client

    def post_cart_add(self, product_id: str, quantity:str):
        data = {'product_id':product_id,
                'quantity': quantity}
        response = self.client.session.post(f"{self.client.base_url}api/sale/cart.add",
                                           data=data)
        return response


    def post_cart_edit(self, key_id: str, quantity:str):
        data = {'key': key_id,
                'quantity': quantity}
        response = self.client.session.post(f"{self.client.base_url}api/sale/cart.edit",
                                           data=data)
        return response

    def post_cart_remove(self, key_id: str):
        data = {'key': key_id}
        response = self.client.session.post(f"{self.client.base_url}api/sale/cart.remove",
                                           data=data)
        return response