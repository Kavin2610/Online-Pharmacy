from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from item.models import Category, Item, Prescription, Rating, Coupon
from core.models import HealthTip
from item.forms import NewItemForm, EditItemForm, CouponForm
from django.db.models import Q

@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'dashboard/index.html', {
        'items': items,
    })

def dashboard_view(request):
    item_count = Item.objects.all().count()
    users_count = User.objects.all().count()
    categories_count = Category.objects.all().count()
    health_tips_count = HealthTip.objects.all().count()
    prescription_count = Prescription.objects.all().count()
    rating_count = Rating.objects.all().count()
    coupon_count = Coupon.objects.all().count()


    return render(request, 'dashboard/dashboard.html',{
        'item_count':item_count,
        'users_count': users_count,
        'categories_count': categories_count,
        'health_tips_count': health_tips_count,
        'prescription_count':prescription_count,
        'rating_count': rating_count,
        'coupon_count': coupon_count,

    })
def users(request):
    admin_users = User.objects.filter(is_superuser=True)
    ordinary_users = User.objects.exclude(Q(is_superuser=True) | Q(is_staff=True))
    staff_users = User.objects.filter(is_staff = True)


    return render(request, 'dashboard/users.html',{
        'admin_users': admin_users,
        'ordinary_users': ordinary_users,
        'staff_users': staff_users


    })

def prescriptions(request):

    prescriptions = Prescription.objects.all()
    return render(request, 'dashboard/prescription.html', {
        'prescriptions':prescriptions,
    })
def products(request):
    products = Item.objects.all()
    
    return render(request, 'dashboard/products.html', {
        'products': products,
    })

def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New item',
    })

@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)

    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()

            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit item',
    })

@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()

    return redirect('dashboard:index')

#coupon system
def coupon(request):
    coupons = Coupon.objects.all()
    


    return render(request, 'dashboard/coupon.html', {
        'coupons': coupons,
    })
    

def add_coupon(request):
    return render(request, 'dashboard/addcoupon.html')

def create_coupon(request):
    item = Item.objects.all()
    if request.method == 'POST':
        form = CouponForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard:coupon')  # Redirect to the coupons page after successful creation
        else:
            print("Form is invalid:", form.errors) 
    else:
        form = CouponForm()
    return render(request, 'dashboard/addcoupon.html', {'form': form, 'items':item})


def delete_coupon(request, pk):
    coupon = get_object_or_404(Coupon,pk=pk)
    coupon.delete()
    return redirect('dashboard:coupon')
    