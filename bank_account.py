class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds the current balance."""
    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(
            f"Cannot withdraw {amount:.2f}: insufficient funds (balance: {balance:.2f})"
        )


class BankAccount:
    transaction_fee = 0.30

    def __init__(self, owner: str, initial_balance: float = 0.0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self._balance = initial_balance
        self.owner = owner

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        total = amount + self.transaction_fee
        if total > self._balance:
            raise InsufficientFundsError(amount, self._balance)
        self._balance -= total

    @classmethod
    def from_dict(cls, data: dict):
        return cls(owner=data["owner"], initial_balance=data.get("balance", 0.0))

    def __str__(self):
        return f"BankAccount(owner='{self.owner}', balance={self._balance:.2f})"

    def __repr__(self):
        return f"BankAccount(owner={self.owner!r}, initial_balance={self._balance!r})"
