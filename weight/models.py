from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Weight(models.Model):
    """A typical class defining a model, derived from the Model class."""

    # Fields
    date = models.DateTimeField(default=timezone.now)
    weight = models.FloatField()
    bodyfat = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Metadata
    class Meta:
        ordering = ['-date']

    # Methods
    def __str__(self):
        return f'{self.date} {self.weight} {self.bodyfat} {self.user}'
