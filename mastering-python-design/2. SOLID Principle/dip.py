#code not following dip
class Email:
    def send_email(self,message:str):
        self.send_email(message)

class Notification:
    def __init__(self) -> None:
        self.email = Email()
    def send(self,message):
        self.email.send_email(message)

#code that follow dip
from abc import ABC,abstractmethod
class MessageSender(ABC):
    @abstractmethod
    def send(self,message:str):
        pass

class Email(MessageSender):
    def send(self, message: str):
        print(f"Sending Email: {message}...")

class Notification:
    def __init__(self, sender:MessageSender) -> None:
        self.sender = sender

    def send(self,message:str):
        self.sender.send(message)

if __name__ == "__main__":
    email = Email()
    notification = Notification(sender=email)
    notification.send(message="This is the DIP example")