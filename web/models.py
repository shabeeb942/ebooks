from django.db import models

# Create your models here.
class Products(models.Model):
    LANG_CHOICES = (
        ('English', 'English'),
        ('Malayalam', 'Malayalam'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()
    old_price = models.DecimalField(decimal_places=2, max_digits=10)
    discount = models.DecimalField(decimal_places=2, max_digits=10)
    cover_page_photo = models.ImageField(upload_to='books')
    hover_image = models.ImageField(upload_to='books')
    book_description = models.TextField()
    book_pdf = models.FileField(upload_to=None)
    language = models.CharField(max_length=50, choices=LANG_CHOICES)
    
    
    def __str__(self):
        return self.name
    

