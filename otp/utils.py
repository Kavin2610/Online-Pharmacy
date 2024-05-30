from django.core.mail import send_mail
from random import randint
from django.conf import settings 
from .models import *

# def generate_otp(user):
#     code = randint(100000, 999999)
#     otp = OTP.objects.create(user=user, code=code)

#     send_mail(
#         subject="your Email Verification for Oneyes Pharmacy",
#         message="Your OTP for verification is {code}",
#         from_email='reachtokavin@gmail.com',
#         to_email = [user.email],
#         fail_silently=False,
#     )
#     return otp