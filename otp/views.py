from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .utils import generate_otp


# def verify_otp(request, otp_id):
#     otp_obj = OTP.objects.get(pk=otp_id)
#     if request.method == "POST":
#         form = OTPForm(request.POST)
#         if form.is_valid():
#             user_otp = form.cleaned_data['otp']
#             if otp_obj.code == user_otp and otp_obj.is_valid:
#                 otp_obj.is_valid = False
                