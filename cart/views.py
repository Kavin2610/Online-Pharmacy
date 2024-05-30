# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import  Cart, CartItem, Item, checkout
from item.models import Coupon
from .forms import CheckoutForm
from django.contrib import messages
from django.conf import settings
import stripe
from django.http import JsonResponse, HttpResponseBadRequest

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Item, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    if not created and cart.user != request.user:
        cart.cartitem_set.all().delete()
        cart.user = request.user  
        cart.save()

   
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, Item=product)
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()

    return render(request, 'cart.html', {'cart_items': [cart_item]})


@login_required
def cart_view(request, discount=None): 
    user_cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=user_cart)
    total_amount = sum(item.total_price for item in cart_items )
    if discount:
        total_amount -= discount
        print(discount)
    return render(request, 'cart.html', {'cart_items': cart_items,'user_cart':user_cart, 'total_amount': total_amount, 'discount': discount})
    
@login_required
def remove_from_cart(request, product_id):
    cart = Cart.objects.get(user=request.user)  
    product = get_object_or_404(Item, id=product_id)
    cart_item = get_object_or_404(CartItem, cart=cart, Item=product)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return render(request, 'cart.html', {'cart_items': [cart_item]})
    #return render(request, 'cart.html', {'cart_items': [cart_item], 'cart_items': cart_items})
def cart(request):
    return render(request, 'cart.html')

def Checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('checkout.html')
    else:
        form = CheckoutForm()
    return render(request, 'checkout.html', {'form' : form})



def submit(request):
    return render(request, 'paymentportal.html')

# def cart_checkout(request):
#     # Retrieve cart items and total amount
#     user_cart = Cart.objects.get(user=request.user)
#     cart_items = CartItem.objects.filter(cart=user_cart)
#     total_amount = sum(item.total_price for item in cart_items )
    
    

#     # Create Stripe Checkout Session
#     stripe.api_key = settings.STRIPE_SECRET_KEY
#     session = stripe.checkout.Session.create(
#         line_items=[
#             {
#                 'price_data': {
#                     'currency': 'inr',
#                     'product_data': {
#                         'name': item.Item,
#                     },
#                     'unit_amount': int(item.total_price * 100),  # Convert to cents
#                 },
#                 'quantity': item.quantity,
#             } for item in cart_items
#         ],
#         mode='payment',
#         success_url='success.html',
#         cancel_url='cancel.html',
#     )

#     context = {'session_id': session.id}
#     return render(request, 'checkout.html', context)



# from django.http import JsonResponse
# from django.shortcuts import get_object_or_404

# def update_quantity(request):
#     if request.method == 'POST':
#         if request.is_ajax():  # Check if it's an AJAX request
#             cart_item_id = request.POST.get('cart_item_id')
#             action = request.POST.get('action')

#             cart_item = get_object_or_404(Cart, id=cart_item_id)

#             if action == 'increase':
#                 cart_item.quantity += 1
#             elif action == 'decrease':
#                 cart_item.quantity -= 1
#                 if cart_item.quantity <= 0:
#                     cart_item.delete()

#             cart_item.save()
    

#             # You can customize the response based on your needs
#             response_data = {'message': 'Cart item updated successfully'}
#             return JsonResponse(response_data)
#         else:
#             return HttpResponseBadRequest('Invalid request type')
#     else:
#         return HttpResponseBadRequest('Invalid request method')
def success(request):
    return render(request, 'cart/success.html')

def cancel(request):
    return render(request, 'cart/cancel.html')

def offer(request):
    coupon1 = "ONEYES100"
    coupon2 = "ONEYES500"

def checkout2(request):
    return render(request, 'chekout2.html')
def cart_checkout(request):
    pass
def update_quantity(request):
    pass

# def checkout(request):
#     if request.method == "POST":
#         token = request.POST.get('stripeToken')
#         amount = 1000
#         stripe.api_key = settings.STRIPE_SECRET_KEY

#         try:
#             charge = stripe.Charge.create(
#                 amount = amount,
#                 currency= 'inr',
#                 description = "test",
#                 source = token,
#             )
#             return redirect('success')
#         except stripe.error.CardError as e:
#             return redirect('cancel')
        
def apply_coupon(request):
    if request.method == "POST":
        coupon_entered = request.POST.get('coupon_code')
        
        try:
            coupon = Coupon.objects.get(coupon_code = coupon_entered)
            discount = coupon.coupon_value
            coupon.usage_count += 1
            return redirect('cart:cart_view', discount = int(discount))
        except Coupon.DoesNotExist:
            messages.error(request, "The coupon is invalid or Expired Please Try with a valid coupon")
    return redirect('cart:cart_view')

    
def create_checkout_session(request):
    # Retrieve amount from request or calculate based on cart items
    amount = 10000  # Amount in cents (e.g., $100)

    # Create a Checkout session
    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'unit_amount': amount,
                'product_data': {
                    'name': 'Your Product',
                    'description': 'Description of your product',
                },
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url='https://yourwebsite.com/success',
        cancel_url='https://yourwebsite.com/cancel',
    )

    return JsonResponse({'id': session.id})