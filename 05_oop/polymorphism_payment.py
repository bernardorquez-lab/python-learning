class Payment:
    label = 'Payment'

    def __init__(self, account):
        self.account = account

    def pay(self, amount):
            print("Payment method not implemented")

    def __str__(self):
        masked = "*" * (len(self.account)-4) + self.account[-4:]
        return f'{self.label:<7}({masked})'


class CashPayment(Payment):
    label = 'Cash'

    def pay(self, amount):
        print(f"Cash {self} -> Paid {amount:.2f} in cash.")


class CardPayment(Payment):
    label = 'Card'
    FEE_RATE = 0.02

    def pay(self, amount):
        print(f"Card {self} -> Charged {amount * self.FEE_RATE + amount:.2f} (includes 2% fee).")


class GCashPayment(Payment):
    label = 'GCash'
    FLAT_FEE = 15.00

    def pay(self, amount):
        print(f"GCash {self} -> Charged {amount + self.FLAT_FEE:.2f} (includes PHP {self.FLAT_FEE:.2f} fee).")


def checkout(payment, amount):
    payment.pay(amount)

if __name__ == "__main__":

    payments = [CashPayment('1234554321'),
                CardPayment('4111111119876'),
                GCashPayment('09171235555')]

    for p in payments:
        p.pay(1000)

