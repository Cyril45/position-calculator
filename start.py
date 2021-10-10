from backend.moneymanagement import MoneyManagement
from frontend.interface import Interface

if __name__ == "__main__":
    fields = (
        "Capital",
        "Percent investment",
        "Ratio risk",
        "Minimal buy",
        "Take profit",
        "Buyed price",
        "Stop loss",
    )
    test = Interface(fields)
