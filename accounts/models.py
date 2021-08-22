from django.core.mail import send_mail
from django.db import models

from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created

# USER_TYPE_CHOICES = (
#     ('student', 'student'),
#     ('teacher', 'teacher'),
#     ('admin', 'admin'),
# )


# class User(AbstractUser):
#     user_type = models.CharField(max_length=40, choices=USER_TYPE_CHOICES)

#     # replacement operator use
#     def __str__(self):
#         return '{}{}'.format(self.username, self.user_type)


# # Create your models here.
class User(AbstractUser):
    is_Admin = models.BooleanField(default=False)
    is_Teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)

#
# class Admin(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     phone = models.BigIntegerField()
#     email = models.EmailField()
#
#
# class Teacher(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     phone = models.BigIntegerField()
#
#     def __str__(self):
#         return self.user.username
#
#
# class Student(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#
#
#     def __str__(self):
#         return self.user.username


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'),
                                                   reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
