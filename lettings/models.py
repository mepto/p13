from django.core.validators import MaxValueValidator, MinLengthValidator
from django.db import models


class Address(models.Model):
    """Store addresses for lettings."""
    number = models.PositiveIntegerField(validators=[MaxValueValidator(9999)])
    street = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2, validators=[MinLengthValidator(2)])
    zip_code = models.PositiveIntegerField(validators=[MaxValueValidator(99999)])
    country_iso_code = models.CharField(max_length=3, validators=[MinLengthValidator(3)])

    def __str__(self):
        """Set default return string for Address object."""
        return f'{self.number} {self.street}'

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'


class Letting(models.Model):
    """Store lettings."""
    title = models.CharField(max_length=256)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    def __str__(self):
        """Set default return string for Letting object."""
        return self.title
