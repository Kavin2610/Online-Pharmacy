from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class OTP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length = 6)
    created_at = models.DateTimeField(auto_now_add = True)
    is_valid = models.BooleanField(default= True)

    def __str__(self):
        return f"{self.user.username} - {self.code}"