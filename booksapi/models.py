from django.db import models


# Create your models here.
class BooK(models.Model):
   bookId = models.AutoField(primary_key=True, unique=True, auto_created=True)
   bookName = models.CharField(max_length=50, null=True)
   AuthorName = models.CharField(max_length=50, null=True)
   rate = models.FloatField(null=True)
   startDate = models.DateField(null=True)
   endDate = models.DateField(null=True)
   status = models.CharField(max_length=50, null=True)
   bookImage = models.ImageField(blank=True)
   
   
   def __str__(self):
      return self.bookName
  
   