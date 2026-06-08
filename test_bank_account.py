from bank_account import BankAccount, InsufficientFundsError

def test_constructor_defaults():
    acc = BankAccount("Alice")
    assert acc.balance == 0.0
    assert acc.owner == "Alice"
    print("PASS: constructor defaults")

def test_constructor_with_balance():
    acc = BankAccount("Bob", 100.0)
    assert acc.balance == 100.0
    print("PASS: constructor with initial balance")

def test_negative_initial_balance():
    try:
        BankAccount("Eve", -50)
        print("FAIL: should have raised ValueError")
    except ValueError:
        print("PASS: negative initial balance raises ValueError")

def test_balance_is_read_only():
    acc = BankAccount("Carol", 50.0)
    try:
        acc.balance = 999
        print("FAIL: balance should be read-only")
    except AttributeError:
        print("PASS: balance is read-only")

def test_deposit():
    acc = BankAccount("Dave", 100.0)
    acc.deposit(50.0)
    assert acc.balance == 150.0
    print("PASS: deposit")

def test_deposit_non_positive():
    acc = BankAccount("Dave", 100.0)
    try:
        acc.deposit(-10)
        print("FAIL: should raise ValueError")
    except ValueError:
        print("PASS: deposit non-positive raises ValueError")

def test_withdraw():
    acc = BankAccount("Frank", 100.0)
    acc.withdraw(50.0)
    # 100 - 50 - 0.30 fee = 49.70
    assert round(acc.balance, 2) == 49.70
    print("PASS: withdraw (fee deducted)")

def test_withdraw_non_positive():
    acc = BankAccount("Grace", 100.0)
    try:
        acc.withdraw(0)
        print("FAIL: should raise ValueError")
    except ValueError:
        print("PASS: withdraw non-positive raises ValueError")

def test_withdraw_insufficient_funds():
    acc = BankAccount("Heidi", 10.0)
    try:
        acc.withdraw(10.0)  # 10 + 0.30 fee > 10
        print("FAIL: should raise InsufficientFundsError")
    except InsufficientFundsError as e:
        print(f"PASS: insufficient funds raises InsufficientFundsError — {e}")

def test_transaction_fee_class_attr():
    assert BankAccount.transaction_fee == 0.30
    print("PASS: transaction_fee class attribute")

def test_from_dict():
    acc = BankAccount.from_dict({"owner": "Ivan", "balance": 200.0})
    assert acc.owner == "Ivan"
    assert acc.balance == 200.0
    print("PASS: from_dict")

def test_from_dict_no_balance():
    acc = BankAccount.from_dict({"owner": "Judy"})
    assert acc.balance == 0.0
    print("PASS: from_dict defaults balance to 0.0")

def test_str():
    acc = BankAccount("Karl", 75.5)
    s = str(acc)
    assert "Karl" in s and "75.50" in s
    print(f"PASS: __str__ → {s}")

def test_repr():
    acc = BankAccount("Laura", 42.0)
    r = repr(acc)
    assert "Laura" in r
    print(f"PASS: __repr__ → {r}")


if __name__ == "__main__":
    print("=== BankAccount Tests ===\n")
    test_constructor_defaults()
    test_constructor_with_balance()
    test_negative_initial_balance()
    test_balance_is_read_only()
    test_deposit()
    test_deposit_non_positive()
    test_withdraw()
    test_withdraw_non_positive()
    test_withdraw_insufficient_funds()
    test_transaction_fee_class_attr()
    test_from_dict()
    test_from_dict_no_balance()
    test_str()
    test_repr()
    print("\n=== All tests complete ===")
