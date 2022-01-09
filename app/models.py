from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
# custom user model
class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password=None, first_name=None, last_name=None):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,)
    first_name = models.CharField(verbose_name='first name',max_length=255,)
    last_name = models.CharField(verbose_name='last name',max_length=255,)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Images(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    file = models.ImageField(upload_to ='app/static/uploads/')
    annotations = models.JSONField(default=None, null=True)

class Annotation(models.Model):
    image = models.ForeignKey(Images, on_delete=models.CASCADE)
    start_x = models.FloatField()
    end_x = models.FloatField()
    start_y = models.FloatField()
    end_y = models.FloatField()
