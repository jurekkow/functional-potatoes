import bestpotato


def test_drop_unneeded_fields():
    potato = {"kind": None, "price": None, "garbage": None}
    expected_potato = {"kind": None, "price": None}
    assert bestpotato.drop_unneeded_fields(potato) == expected_potato


def test_extract_kind_name():
    potato = {"kind": '{"name": "test potato"}', "price": 3000}
    expected_potato = {"kind": "test potato", "price": 3000}
    assert bestpotato.extract_kind_name(potato) == expected_potato


def test_extract_kind_name_from_info_field():
    potato = {"kind": '{"info": {"name": "test potato"}}', "price": 3000}
    expected_potato = {"kind": "test potato", "price": 3000}
    assert bestpotato.extract_kind_name(potato) == expected_potato


def test_convert_price_to_kg():
    potato = {"price": 3000, "kind": "test potato"}
    expected_potato = {"price": 3.0, "kind": "test potato"}
    assert bestpotato.convert_to_price_per_kg(potato) == expected_potato


def test_format_kind_name_for_non_premium_potato():
    price = bestpotato.PREMIUM_MIN_PRICE - 1
    potato = {"price": price, "kind": "test potato"}
    expected_potato = {"price": price, "kind": "Test Potato"}
    assert bestpotato.format_kind_name(potato) == expected_potato


def test_format_kind_name_for_premium_potato():
    price = bestpotato.PREMIUM_MIN_PRICE
    potato = {"price": price, "kind": "test potato"}
    expected_potato = {"price": price, "kind": "Test Potato (Premium)"}
    assert bestpotato.format_kind_name(potato) == expected_potato


def test_map_field_names():
    potato = {"price": 3.0, "kind": "test potato"}
    expected_potato = {"priceKg": 3.0, "name": "test potato"}
    assert bestpotato.map_field_name(potato) == expected_potato
