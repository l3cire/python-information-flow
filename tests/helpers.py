def assert_val_level(sec_type, expected_val, expected_level):
    assert sec_type.get_value() == expected_val
    assert sec_type.get_level() == expected_level
