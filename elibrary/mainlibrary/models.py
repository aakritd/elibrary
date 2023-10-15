from django.db import models

# Create your models here.

class book(models.Model):
    book_name = models.CharField(max_length=150)
    pdf_file = models.FileField(upload_to='books/',max_length=250,null = True,default = None)