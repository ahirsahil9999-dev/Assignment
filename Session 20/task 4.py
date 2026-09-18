# Create an abstract class PaymentMethod with an abstract method
# pay(amount). Then, create two subclasses: UPI and CreditCard, 
# each implementing the pay method with a print statement showing
# how the payment would be processed.<br><br><em><strong>Hint:
# </strong> Use the abc module for abstraction.</em>

from abc import ABC, abstractmethod


class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class UPI(PaymentMethod):
    def pay(self, amount):
        print("Payment of", amount, "processed using UPI")


class CreditCard(PaymentMethod):
    def pay(self, amount):
        print("Payment of", amount, "processed using Credit Card")


upi = UPI()
card = CreditCard()

upi.pay(500)
card.pay(1000)