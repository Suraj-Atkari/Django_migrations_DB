from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name} ({self.code})"

    class Meta:
        verbose_name_plural = "Countries"


class Address(models.Model):
    street = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=80)
    city = models.CharField(max_length=50)

    def Complete_Address(self):
        return f"{self.street}, {self.city}: {self.postal_code}"

    def __str__(self):
        return self.Complete_Address()

    class Meta:
        verbose_name_plural = "Address Entriess"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(
        "Address", null=True, on_delete=models.CASCADE)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    title = models.CharField(max_length=55)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books")
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    published_countries = models.ManyToManyField(Country)

    def get_absolute_url(self):
        return reverse("book-details", args=[self.slug])

    # def save(self, *args, **kwargs):        #removed because we have admin class pre_popullated fiedls
    #     self.slug = slugify(self.title)
    #     return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} {self.rating}'
