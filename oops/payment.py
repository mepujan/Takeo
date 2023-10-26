class Payment:
    def process_payment(self):
        print("Processing the payment.")


class CreditCardPayment(Payment):
    def process_payment(self):
        print("Processing Credit Card Payment")


class CashPayment(Payment):
    def process_payment(self):
        print("Processing Cash Payment")


class PaypalPayment(Payment):
    def process_payment(self):
        print("Processing Paypal Payment")


payment_methods = ["Credit", "Cash", "Paypal"]
print("1. Credit")
print("2. Cash")
print("3. Paypal")
choice = int(input("Enter the choice: "))
match choice:
    case 1:
        credit_card = CreditCardPayment()
        credit_card.process_payment()
    case 2:
        cash = CashPayment()
        cash.process_payment()
    case 3:
        paypal = PaypalPayment()
        paypal.process_payment()
    case _:
        print("Invalid Input. Try Again.")
