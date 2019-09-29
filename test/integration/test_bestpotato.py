import bestpotato


def test_get_parsed_potatoes():
    expected_potatoes = [
        {"name": "Russer", "priceKg": 1.1},
        {"name": "Austrian Crescent (Premium)", "priceKg": 5.08},
    ]
    assert bestpotato.get_parsed_potatoes() == expected_potatoes
