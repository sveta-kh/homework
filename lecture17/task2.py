#Online payment

class Payment:
    def process_payment(self, amount):
        print("Payment is in process")

class CreditCardPayment(Payment):
    def process_payment(self, emount):
        print(f"Paid with a Credit Card: {emount}Gel") 

class PayPalPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid with a PayPal: {amount}Gel")

card = CreditCardPayment()
paypal = PayPalPayment()

card.process_payment(500)
paypal.process_payment(400)


                   
        