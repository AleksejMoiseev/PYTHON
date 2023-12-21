from abc import ABC
from abc import abstractmethod


class Order:
    def pay(self, strategy: "PaymentStrategy", amount: int):
        strategy.pay(amount)


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount): pass


class PayPalPaymentStrategy(PaymentStrategy):
    def __init__(self, email, token):
        self.email = email
        self.token = token

    def pay(self, amount):
        print(f"processing {amount}$ via PayPal")


class PayNalaymentStrategy(PaymentStrategy):

    def __init__(self, nal):
        self.nal = nal

    def pay(self, amount):
        print(f"processing {amount}$ via Nal")


o = Order()
paypal_strategy = PayPalPaymentStrategy("email", "token")
nal_strategy = PayNalaymentStrategy("nal")
o.pay(strategy=paypal_strategy, amount=20)
o.pay(strategy=nal_strategy, amount=10)