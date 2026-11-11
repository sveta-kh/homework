import pytest
from bank import BankAccount

@pytest.fixture
def account():
    return BankAccount("Sveta", 100.0)

def test_initial_balance():
    defoult_account = BankAccount("sveta")
    assert defoult_account.balance == 0.0

def test_deposit_success(account):
    account.deposit(50.0)
    assert account.balance == 150.0

def test_deposit_negative(account):
    with pytest.raises(ValueError, match="Amount must be positive"):
        account.deposit(-100.0)
    with pytest.raises(ValueError, match="Amount must be positive"):    
        account.deposit (0.0)

def test_withdraw_success():
    account = BankAccount("Sveta", 200.0)
    account.withdraw(50.0)
    assert account.balance == 150.0

def test_withdraw_insufficient_funds(account):
    with pytest.raises(ValueError, match="Balance is not enough"):
        account.withdraw(150.0)

def test_withdraw_negative(account):
    with pytest.raises(ValueError, match="Amount must be positive"):
        account.withdraw(-150.0)












