from django.shortcuts import render, redirect
from item.models import Category, Item, Prescription
from .models import HealthTip  
from django.contrib.auth import logout
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_protect
from django.utils.http import urlencode
from django.template.loader import render_to_string
from django.urls import reverse
from django.core.mail import send_mail
from django.http import HttpResponse
from .forms import *
import uuid
from .forms import SignupForm, AdditionalInfoForm
#ai chat bot integration
import textwrap
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from IPython.display import Markdown
import google.generativeai as genai

api = "AIzaSyALn45I1d7q2pBnY-LdA_w8xfP8tQbbYWc"
GOOGLE_API_KEY = api
genai.configure(api_key=GOOGLE_API_KEY)

def to_markdown(text):
    text = text.replace('.', ' *')
    return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
def chat_view(request):
    if request.method == 'POST':
        data = request.POST.get('user-query')
        response = process_chat_query(data)
        markdown_response = to_markdown(response.text)
        
        return JsonResponse({'response': str(markdown_response)})
    else:
        return render(request, 'core/chat.html')

def process_chat_query(query):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(query)
    return response

def index(request):
    items = Item.objects.filter(is_sold=False)[0:20]
    categories = Category.objects.all()
    health_tips = HealthTip.objects.all()
    

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
        'health_tips': health_tips,

    })



from django.shortcuts import render, redirect
from .forms import ContactUsForm

def contact(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to the same page after form submission
    else:
        form = ContactUsForm()
    return render(request, 'core/contact.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = SignupForm()



    return render(request, 'core/signup.html', {
        'form': form
    })

def about(request):
    return render(request, 'core/about.html')

def privacy(request):
    return render(request, 'core/privacy.html')

def test(request):
    return render(request, 'core/test.html')

def pharmacistlogin(request):
    return render(request, 'core/pharmacist.html')

def pharmacist_prescriptions(request):
    all_prescriptions = Prescription.objects.all()
    return render(request, 'pharmacist.html', {'prescription': all_prescriptions})


from .models import UserProfile

def myprofile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = AdditionalInfoForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to the same page after saving
    else:
        form = AdditionalInfoForm(instance=user_profile)
    return render(request, 'core/myprofile.html', {'form': form, 'user_profile': user_profile })



@csrf_protect
def custom_logout(request):
    logout(request)
    return redirect('/')




