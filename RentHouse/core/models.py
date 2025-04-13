from django.db import models
from django.contrib.auth.models import(AbstractBaseUser ,
                                        PermissionsMixin ,
                                        BaseUserManager
)
from uuid import uuid4
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            email = self.normalize_email(email)
        username = username
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)


class Tenant(AbstractBaseUser, PermissionsMixin):
    
    username          = models.CharField(max_length=255 , unique=True)
    email             = models.EmailField(blank=True)
    phone_number      = models.CharField(max_length=8 , unique=True)
    is_staff          = models.BooleanField(default=False)
    age               = models.PositiveBigIntegerField()
    identity_card_num = models.CharField(max_length=10 , unique=True)
    is_active         = models.BooleanField(default=True)
    sec_field         = models.CharField(max_length=250 , default=uuid4)
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username
    

class Department(models.Model) :
    name     = models.CharField(max_length=255 , unique=True)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class House(models.Model) :
    TYPE_CHOICES = (
        ('s+1','s+1'),
        ('s+2','s+2'),
        ('s+3','s+3'),
    )
    description     = models.TextField()
    type            = models.CharField(max_length=15 , choices=TYPE_CHOICES)
    price_per_month = models.DecimalField(max_digits=6 , decimal_places=2)
    available       = models.BooleanField(default=True , null=True)
    department      = models.ForeignKey(Department , on_delete=models.CASCADE , related_name="house")

    def __str__(self) :
        return self.type

class HouseImage(models.Model) :
    house  = models.ForeignKey(House , on_delete=models.CASCADE , related_name="images")
    images = models.ImageField(upload_to="house")    


class Rent(models.Model) :
    tenant = models.ForeignKey(Tenant , on_delete=models.CASCADE ,related_name='rent')
    house  = models.ForeignKey(House , on_delete=models.CASCADE , related_name='rent')

    def __str__(self) :
        return f"{self.tenant.user.username} rent a {self.house.type}"