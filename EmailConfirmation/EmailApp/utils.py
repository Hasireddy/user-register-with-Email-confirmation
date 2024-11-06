from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string


def send_confirmation_mail(request, user):
    subject = "Confirm your Email"
    # generates a unique token for the user
    token = default_token_generator.make_token(user)
    # Encoding User id to safely pass in the Url
    user_id = urlsafe_base64_encode(force_bytes(user.id))
    # Constructs an absolute Url by reversing a named Url pattern and appending User id and token as Url parameters.The reverse() function generates a URL dynamically for a given view based on its name and any arguments (if required) passed to it.
    confirmation_link = request.build_absolute_uri(
        reverse("EmailApp:confirm_email", kwargs={"user_id": user_id, "token": token})
    )
    # The HTML version is rendered using render_to_string
    html_message = render_to_string(
        "EmailApp/email_confirm.html",
        {
            "user": user,
            "confirmation_link": confirmation_link,
        },
    )

    # extract the plain text version of the email, which is important for email clients that do not support HTML.
    message = strip_tags(html_message)

    # send_mail sends the email using the provided subject, message, and HTML message
    send_mail(
        subject=subject,
        from_email=None,
        recipient_list=[user.email],
        message=message,
        html_message=html_message,
    )
