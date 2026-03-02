import pytest
from bankapp import transfer, calculate_interest


def test_transfer_valid():
    from_balance, to_balance = transfer(5000, 2000, 1000)
    assert from_balance == 4000
    assert to_balance == 3000


def test_transfer_invalid_amount():
    with pytest.raises(ValueError):
        transfer(5000, 2000, 0)


def test_transfer_then_interest():
    from_balance, to_balance = transfer(5000, 2000, 1000)
    new_balance = calculate_interest(to_balance, 10, 1)
    assert round(new_balance, 2) == 3300.0