import allure
import pytest


@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.parametrize(
    "firstname, lastname, address_1, city, country_id, zone_id",
    [
        ("Customer", "Dear", "Somewhere", "KLD", "RUS", 1),
        ("", "Dear", "Somewhere", "KLD", "RUS", 3),
        ("Customer", "", "Somewhere", "KLD", 10, "KGD"),
        ("Customer", "Dear", "", "KLD", "RUS", 123),
        ("Customer", "Dear", "Somewhere", "", "RUS", 99),
        ("Customer", "Dear", "Somewhere", "KLD", "", "KGD"),
        ("Customer", "Dear", "Somewhere", "KLD", 55, ""),
        ("", "", "", "", "", ""),
        ("John", "Doe", "Street 123", "NY", "USA", 1056),
        ("Alice", "Smith", "Main St", "LA", "USA", 0),
        ("123", "456", "789", "000", "AAA", "BBB"),
    ]
)
@allure.step("Testing post_payment_address")
def test_post_payment_address(client, firstname, lastname, address_1, city, country_id, zone_id):
    response = client.payment_api.post_payment_address(
        firstname=firstname,
        lastname=lastname,
        address_1=address_1,
        city=city,
        country_id=country_id,
        zone_id=zone_id
    )
    if not firstname:
        assert response.json()['error']['firstname']  == 'First Name must be between 1 and 32 characters!'
    if not lastname:
        assert response.json()['error']['lastname']  == 'Last Name must be between 1 and 32 characters!'
    if not address_1:
        assert response.json()['error']['address_1'] == 'Address 1 must be between 3 and 128 characters!'
    if not city:
        assert response.json()['error']['city'] == 'City must be between 3 and 128 characters!'
    if not country_id:
        assert response.json()['error']['country'] == 'Please select a country!'
    if not zone_id:
        assert response.json()['error']['zone'] == 'Please select a region / state!'
    assert response.status_code == 200



