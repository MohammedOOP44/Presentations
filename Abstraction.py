from abc import ABC , abstractmethod
class Paymentprocessor(ABC):

    @abstractmethod 
    def process_payment(self,amount):
        pass

    def print_receipt(self,amount):
        print(f"Receipt generated for: ${amount}")

class PayPalProcessor(Paymentprocessor):
    def process_payment(self,amount):
        print(f"processing ${amount} securely via PayPal API ...")

paypal = PayPalProcessor()
paypal.process_payment(100)
paypal.print_receipt(100)
    
