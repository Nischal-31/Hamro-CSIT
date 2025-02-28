from allauth.account.signals import user_signed_up,user_logged_in
from django.core.mail import send_mail
from django.dispatch import receiver
from django.template.loader import render_to_string

from django.db.models.signals import post_save
from allauth.socialaccount.signals import social_account_added
from django.contrib.auth import get_user_model

@receiver(user_signed_up)
def send_welcome_email(sender, request, user, **kwargs):
    subject = 'Welcome to Our Website'
    from_email = 'xenobaka2@gmail.com'
    to_email = user.email

    # Create the email content using a template
    html_content = render_to_string('user/Email.html', {'username': user.username})

    # Send the email
    send_mail(subject, '', from_email, [to_email], html_message=html_content)

@receiver(user_logged_in)
def set_user_type_on_login(sender, request, user, **kwargs):
    """ Set user_type as 'normal' if the user logged in with Google """
    if hasattr(user, 'socialaccount_set') and user.socialaccount_set.filter(provider='google').exists():
        user.user_type = 'normal'  # Setting user type to normal
        user.save()

@receiver(social_account_added)
def set_user_type_on_social_login(sender, request, sociallogin, user, **kwargs):
    """ Set user_type as 'normal' if the user logged in with Google """
    if sociallogin.account.provider == 'google':  # Check if login is through Google
        user.user_type = 'normal'
        user.save()
        
@receiver(social_account_added)
def set_default_user_type(sender, request, sociallogin, **kwargs):
    user = sociallogin.user
    # Automatically set the user type to "normal" for Google sign-ups
    if not user.user_type:
        user.user_type = 'normal'
        user.save()