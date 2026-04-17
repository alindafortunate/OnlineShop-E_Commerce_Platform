from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models



class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="perctange value from (0 to 100)",
    )
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    active = models.BooleanField()

    def __str__(self):
        return self.code
