from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg
from django.db.models.functions import Length


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Prescription(models.Model):
    patient_name = models.CharField(max_length=25)
    prescription_images = models.ImageField(upload_to='prescription_images', null=True, blank=True )
    prescription_pdf = models.FileField(upload_to='prescription_pdf', null=True, blank=True)
    message = models.CharField(max_length=200, null = True, blank = True)

    def __str__(self):
       return self.patient_name

class Rating(models.Model):
    RATE_CHOICES = [
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
        ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    score = models.CharField(max_length=10, choices=RATE_CHOICES)
    comment = models.TextField(null=True, blank=True)  
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_average_rating(product):
        
        average_rating = Rating.objects.filter(product=product).annotate(score_length=Length('score')).aggregate(Avg('score_length'))['score_length__avg']

        # Return the average rating or 0 if no ratings exist
        return average_rating or 0
    
    def __str__(self):
        return f"{self.score} : {self.user} : {self.comment}"
    
class Coupon(models.Model):
    coupon_name = models.TextField(null=True, blank=True)
    coupon_code = models.CharField(max_length=50, unique=True)
    coupon_value = models.DecimalField(max_digits = 10, decimal_places = 2, null=True)
    coupon_description = models.TextField(null=True, blank= True)
    valid_from = models.DateTimeField(null=True, blank= True)
    valid_to = models.DateTimeField(null=True, blank = True)
    usage_limit = models.PositiveIntegerField(default = 1)
    usage_count = models.PositiveIntegerField(default = 0)
    applicable_products = models.ManyToManyField('Item', related_name='coupon', blank=True)
    min_purchase_amount = models.DecimalField(max_digits=10, decimal_places = 2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.coupon_name 

