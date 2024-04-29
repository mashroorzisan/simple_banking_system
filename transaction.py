from datetime import datetime
class Transaction:
    def __init__(self, transaction_name, amount) -> None:
        self.transaction_name = transaction_name
        self.amount = amount
        self.time = datetime.now()
    def __repr__(self) -> str:
        return f"{self.transaction_name}-{self.time}"