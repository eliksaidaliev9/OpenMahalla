from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from django.utils import timezone

# Custom User Manager
class UserManager(BaseUserManager):
    # Create a user
    def create_user(self, phone_number, password=None, username=None, **extra_fields):
        if not phone_number:
            raise ValueError("Phone number is required") # Phone number is required
        # Create a model instance
        user = self.model(phone_number=phone_number, username=username, **extra_fields)
        user.set_password(password) # Password hashing
        user.save() # Save to database
        return user

# Create a Superuser
    def create_superuser(self, phone_number, password=None, username=None, **extra_fields):
        # Specifying default fields for creating a superuser
        extra_fields.setdefault('is_staff', True) # Admin panel access right
        extra_fields.setdefault('is_superuser', True) # To have all rights
        # If is_staff is not True, throw an error
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        # If is_superuser is not True, throw an error
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        # Finally, create the user by calling the create_user method.
        return self.create_user(phone_number, password, username, **extra_fields)

# Custom User Model
class User(AbstractUser, PermissionsMixin):
    # User roles
    ROLE_CHOICES = (
        ('applicant', 'Applicant'),
        ('staff', 'Staff'),
        ('admin', 'Admin'),
    )

    phone_number = models.CharField(max_length=15, unique=True, null=True) # Phone number — used as login
    username = models.CharField(max_length=50, unique=True, null=True, blank=True) # Username field (optional)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='applicant') # User role
    date_joined = models.DateTimeField(default=timezone.now) # Registered time
    is_active = models.BooleanField(default=True) # Whether the user is active or not
    is_staff = models.BooleanField(default=False) # Admin panel access rights

    objects = UserManager()

    USERNAME_FIELD = 'phone_number' # Phone number is used as login
    REQUIRED_FIELDS = [] # Required fields when creating a superuser

    # Representing the model as a string
    def __str__(self):
        return self.username if self.username else self.phone_number