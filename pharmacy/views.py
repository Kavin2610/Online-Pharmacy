from django.shortcuts import render
import stripe
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse

def payment_view(request):
    if request.method == 'POST':
        # Handle payment processing here
        # Charge the user's card with a dummy payment
        try:
            charge = stripe.Charge.create(
                amount=1000,  # Amount in cents
                currency='usd',
                source=request.POST['stripeToken'],  # Token from the frontend
                description='Dummy Payment',
            )
        except stripe.error.CardError as e:
            # Handle card errors (e.g., invalid card number)
            pass
        # Handle other exceptions
        return render(request, 'payment/success.html')
    return render(request, 'payment/payment.html')


