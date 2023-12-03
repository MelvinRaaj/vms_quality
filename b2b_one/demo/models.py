from django.db import models

# Create your models here.
class Productss(models.Model):
    title = models.CharField(max_length=150)
    short_description = models.TextField(max_length=100)

    def __str__(self):
        return self.title


class Image(models.Model):
    product = models.ForeignKey(
        Productss, on_delete=models.CASCADE, null=True
        )
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.product.title


class Variant(models.Model):
    product = models.ForeignKey(
        Productss, on_delete=models.CASCADE
        )
    size = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.product.title