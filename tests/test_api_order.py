import pytest
import allure



@allure.step("Testing post add order")
def test_post_order_add(client):
    client.cart_api.post_cart_add(product_id="10", quantity="1")
    response = client.order_api.post_order_add()
    assert response.status_code == 200


