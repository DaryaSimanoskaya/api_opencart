import allure
import pytest


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize("currency, expected_status",
                         [("GBP", 200), ("USD", 200), ("EUR", 200), ("invalid", 400),
                          (" ", 400), (44, 400)])
@allure.step("Testing post_currency")
def test_post_currency(client, currency, expected_status):
    response = client.post_currency(currency=currency)
    assert response.status_code == expected_status
    if response.status_code == 200:
        assert response.json()['success'] == 'Success: Your currency has been changed!'
    else:
        assert response.json()['error'] == 'Warning: Currency could not be found!'

