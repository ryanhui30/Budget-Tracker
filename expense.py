# expenses class file

class Expense:

    def __init__(self, name, category, amount) -> None:     # constructor method
        self.name = name       # 3 info's needed
        self.category = category
        self.amount = amount

    def __repr__(self):     # representation function to output expense memory address
        return f"<Expense: {self.name}, {self.category}, ${self.amount:.2f} >"
