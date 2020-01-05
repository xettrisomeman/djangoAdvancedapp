from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _ 
from django.utils import timezone
from django.urls import reverse
    


from .managers import CustomUserManager


import uuid

class CustomUser(AbstractUser):
    username = None
    first_name = models.CharField(_("first name"), max_length=50)
    last_name = models.CharField(_("last name"), max_length=50)
    email = models.EmailField(_("email address"), max_length=254,unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (first_name , last_name)

    object = CustomUserManager()

    def __str__(self):
        return self.email


class Post(models.Model):
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    post_id = models.UUIDField(default=uuid.uuid4 ,editable=False)
    content = models.TextField()
    created_at = models.DateTimeField(editable=False)
    modified_at = models.DateTimeField(auto_now=True)

    def save(self):
        if not self.id:
            self.created_at = timezone.now()
        return super().save()

    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"post_id": self.post_id})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE , blank=True)
    commented_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE , blank=True)
    created_at= models.DateTimeField(editable=False)
    comment_id = models.UUIDField(default=uuid.uuid4 , editable=False)
    modified_at= models.DateTimeField(auto_now=True)
    comments = models.TextField()

    def save(self):
        if not self.id:
            self.created_on = timezone.now()
        return super().save()
    
    def __str__(self):
        return self.comment_id
    