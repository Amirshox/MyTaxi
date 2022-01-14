import datetime
import uuid

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

phone_regex = RegexValidator(
    regex=r'^998[0-9]{9}$',
    message="Phone number must be entered in the format: '998 [XX] [XXX XX XX]'. Up to 12 digits allowed."
)


def upload_name(instance, filename):
    file_type = filename.split('.')[-1]
    today = str(datetime.datetime.today())[0:7]

    return 'users/photo/%s/%s.%s' % (today, uuid.uuid4(), file_type)


class User(AbstractUser):
    phone_number = models.CharField(max_length=13, validators=[phone_regex])
    photo = models.ImageField(upload_to=upload_name)

    def __str__(self):
        return self.username
