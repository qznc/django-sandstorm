from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, sandstorm_id, name, handle=None):
        if not sandstorm_id:
            raise ValueError('Users must have a sandstorm_id')

        user = self.model(sandstorm_id, name, handle)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self):
        """
        Creates and saves superuser Alice
        """
        user = self.create_user("admin", "Alice Admin", "alice")
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    sandstorm_id = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=256)
    handle = models.CharField(max_length=128, null=True, blank=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'sandstorm_id'

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.handle

    def __str__(self):              # __unicode__ on Python 2
        return self.sandstorm_id

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
