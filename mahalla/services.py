from django.core.exceptions import ValidationError
from .models import Mahalla


def create_mahalla(data):
    if Mahalla.objects.filter(
            name=data['name'],
            district=data['district']
    ).exists():
        raise ValidationError("Mahalla already exists")

    return Mahalla.objects.create(**data)