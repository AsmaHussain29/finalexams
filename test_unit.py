import pytest
from bankapp import (
    deposit,
    withdraw,
    calculate_interest,
    check_loan_eligibility
)

# -------- deposit --------

def test_deposit_valid():
    assert deposit(1000, 500) == 1500

def test_deposit_boundary():
    assert deposit(1000, 1) == 1001

def test_deposit_invalid():
    with pytest.raises(ValueError):
        deposit(1000, 0)


# -------- withdraw --------

def test_withdraw_valid():
    assert withdraw(1000, 400) == 600

def test_withdraw_boundary():
    assert withdraw(1000, 1000) == 0

def test_withdraw_insufficient():
    with pytest.raises(ValueError):
        withdraw(500, 600)

def test_withdraw_invalid_amount():
    with pytest.raises(ValueError):
        withdraw(1000, 0)


# -------- calculate_interest --------

def test_interest_valid():
    result = calculate_interest(1000, 10, 2)
    assert round(result, 2) == 1210.0

def test_interest_boundary():
    assert calculate_interest(0, 10, 2) == 0

def test_interest_invalid_balance():
    with pytest.raises(ValueError):
        calculate_interest(-100, 10, 2)

def test_interest_invalid_rate():
    with pytest.raises(ValueError):
        calculate_interest(1000, -5, 2)


# -------- loan eligibility --------

def test_loan_eligible():
    assert check_loan_eligibility(6000, 750) is True

def test_loan_not_eligible():
    assert check_loan_eligibility(4000, 650) is False

def test_loan_boundary():
    assert check_loan_eligibility(5000, 700) is True

def test_loan_invalid_balance():
    with pytest.raises(ValueError):
        check_loan_eligibility(-100, 750)