from django.core.mail import send_mail, EmailMessage
from django.conf import settings

def send_account_activation_email(email, email_token):
    subject = "Account verification link"
    message = f"click here to verify http://192.168.100.6:8000/accounts/activate/{email_token}"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    print(f"Sending email to {recipient_list[0]} and {email_token}")
    send_mail(subject, message, from_email, recipient_list)
    # mail = EmailMessage(subject, message, from_email, recipient_list)
    # mail.attach_file(f"{settings.BASE_DIR}/file.pdf")
    # mail.send()
    
    
def send_custom_email():
    subject = "First email"
    message = "Hello Hamid how are you"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["hafizhamidahmad1999@gmail.com"]
    send_mail(subject, message, from_email, recipient_list)