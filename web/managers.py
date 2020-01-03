from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _ 



class CustomUserManager(BaseUserManager):

    def create_user(self,email,password,**extra):

        if not email:
            raise ValueError(_('Email is required'))
        email = self.normalize_email(email)
        user = self.model(email=email , **extra)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,password,**extra):

        extra.setdefault('is_superuser' , True)
        extra.setdefault('is_active' , True)
        extra.setdefault('is_staff' , True)

        if extra.get('is_staff') is not True:
            raise ValueError(_("is staff is needed to be True"))
        if extra.get('is_superuser') is not True:
            raise ValueError(_('is superuser is needed to be True'))

        return self.create_user(email , password,**extra)

    