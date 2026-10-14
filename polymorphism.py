# class bkashpayment:
#     def pay(self, amount):
#         print(f"Paid {amount} using Bkash")

# class Cardpayment:
#     def pay(self, amount):
#         print(f"Paid {amount} using card")
# class Banktransfer:
#     def pay(self, amount):
#         print(f"Paid {amount} using bank transfer")

# def process_payment(payment_method, amount):
#     payment_method.pay(amount)

# print("Select payment method: 1. Bkash\n2. Card\n3. Bank Transfer")

# choice = input("Enter your choice (1/2/3): ")
# if choice == '1':
#     payment_method = bkashpayment()
#     process_payment(payment_method, 1200)
# if choice == '2':
#     payment_method = Cardpayment()
#     process_payment(payment_method, 1200)
# if choice == '3':
#     payment_method = Banktransfer()
#     process_payment(payment_method, 1200)
    
# else :
#     if choice not in ['1', '2', '3']:
#      print("Please enter a valid choice (1/2/3).")
#      print("Invalid choice")
    


# simple Notification system using polymorphism

class EmailNotification:
    def send_notification(self, message):
        print(f"Sending email notification: {message}")
    
class SMSNotification:
    def send_notification(self, message):
        print(f"Sending SMS notification: {message}")
class PushNotification:
    def send_notification(self, message):
        print(f"Sending push notification: {message}")

def notify(notification,message):
    notification.send_notification(message)

notify(EmailNotification(), "Your order has been shipped.")
notify(SMSNotification(), "Your order has been shipped.")
notify(PushNotification(), "Your order has been shipped.")