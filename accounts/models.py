from django.db import models
from django.contrib.auth.models import User
from base.models import *
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver
from base.email import send_account_activation_email



class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    is_email_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="profile_images")
    
    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name} - {self.user.username}"
    
@receiver(post_save, sender=User)
def send_email_token(sender, instance, created, **kwargs):
    try:
        if created:
            print("Signal called")
            email_token=str(uuid.uuid4())
            Profile.objects.create(user=instance,  email_token=email_token)
            email=instance.username
            print("Email is: ",email)
            send_account_activation_email(email, email_token)
    except Exception as e:
        print(e)
    
    

    
