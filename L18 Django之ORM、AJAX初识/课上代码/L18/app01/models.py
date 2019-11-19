from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=5, decimal_places=2)  # 999.99
    pub_date = models.DateField()

    def __str__(self):
        return self.title
