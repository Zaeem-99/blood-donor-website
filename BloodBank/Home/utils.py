from Home.models import *
from django.conf import settings

from django.shortcuts import render, redirect


from django.core.mail import send_mail
from django.conf import settings

def send_email_to_donor(donor_email):
    """
    Sends an email to the donor when a user requests contact.
    """
    subject = "Blood Donation Request"
    message = (
        "Hello,\n\n"
        "Someone is interested in contacting you regarding blood donation. "
        "Please check your email for further details.\n\n"
        "Best Regards,\nBlood Donation Team"
    )

    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,  # Sender email from settings
        [donor_email],  # Dynamic recipient
        fail_silently=True,  # Set to True to suppress errors
    )

           


# def send_email_to_donor(request, donor_email):
#     if request.user.is_authenticated:  # Ensure user is logged in
#         subject = "Blood Donation Request"
#         message = f"Hello,\n\nSomeone is interested in contacting you regarding blood donation. Please check your email for further details.\n\nBest Regards,\nBlood Donation Team"
#         from_email = settings.EMAIL_HOST_USER  # Replace with your email
#         recipient_list = ["zaeempathan11@gmail.com"]
#         # recipient_list = [donor_email]

#         try:
#             send_mail(subject, message, from_email, recipient_list)
#             messages.success(request, "Email sent successfully!")
#         except Exception as e:
#             messages.error(request, f"Error sending email: {e}")

#     return redirect("/search-page/")  # Redirect back to search page