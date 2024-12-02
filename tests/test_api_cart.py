import pytest
import allure



@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize(
    "product_id, quantity, expected_status",
    [
        ("40", "1", 200),
        ("40", "0", 200),
        ("", "1", 400),
        ("9999", "1", 400),
        ("40", "", 400),
        ("invalid", "1", 400),
    ]
)
@allure.step("Testing post add to cart with product_id={product_id} and quantity={quantity}")
def test_post_cart_add(client, product_id, quantity, expected_status):
    response = client.cart_api.post_cart_add(product_id=product_id, quantity=quantity)
    assert response.status_code == expected_status
    if response.status_code == 200:
        assert response.json()['success'] == 'Success: You have modified your shopping cart!'
    else:
        assert response.json()['error'] == 'Warning: Product could not be found!'


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize(
    "key_id, quantity, expected_status",
    [
        ("40", "1", 200),
        ("40", "0", 200),
        ("", "1", 400),
        ("9999", "1", 400),
        ("40", "", 400),
        ("invalid", "1", 400),
    ]
)
@allure.step("Testing post edit  cart with key={key_id} and quantity={quantity}")
def test_post_cart_edit(client, key_id, quantity, expected_status):
    response = client.cart_api.post_cart_edit(key_id=key_id, quantity=quantity)
    assert response.status_code == expected_status
    if response.status_code == 200:
        assert response.json()['success'] == 'Success: You have modified your shopping cart!'
    else:
        assert response.json()['error'] == 'Warning: Product could not be found!'


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize(
    "key_id, expected_status",
    [
        ("40", 200),
        ("", 400),
        ("9999", 200),
        ("invalid", 400),
    ]
)
@allure.step("Testing post remove  cart with key={key_id} ")
def test_post_cart_remove(client, key_id, expected_status):
    response = client.cart_api.post_cart_remove(key_id=key_id)
    assert response.status_code == expected_status
    if response.status_code == 200:
        assert response.json()['success'] == 'Success: You have modified your shopping cart!'
    else:
        assert response.json()['error'] == 'Warning: Product could not be found!'