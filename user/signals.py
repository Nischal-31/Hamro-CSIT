from allauth.account.signals import user_signed_up
from django.core.mail import send_mail
from django.dispatch import receiver
from django.template.loader import render_to_string

@receiver(user_signed_up)
def send_welcome_email(sender, request, user, **kwargs):
    subject = 'Welcome to Our Website'
    from_email = 'xenobaka2@gmail.com'
    to_email = user.email

    # Create the email content using a template
    html_content = render_to_string('user/Email.html', {'username': user.username})

    # Send the email
    send_mail(subject, '', from_email, [to_email], html_message=html_content)
