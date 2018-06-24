from django.db import models

# Create your models here.


class  HindiPoem(models.Model):
      AuthorName = models.CharField(max_length=50)

      PoemTitle=models.CharField(max_length=100)

      PoemContent=models.CharField(max_length=1000)


          #def __str__(self):
          #return [self.AuthorName, self.PoemTitle, self.PoemContent]
class EnglishPoem(models.Model):
      AuthorName = models.CharField(max_length=50)

      PoemTitle = models.CharField(max_length=100)

      PoemContent = models.CharField(max_length=1000)


class AddHindiPoem(models.Model):
      AuthorName = models.CharField(max_length=50)

      Type=models.CharField(max_length=10)

      Title=models.CharField(max_length=100)

      Content=models.CharField(max_length=1000)




class AddEnglishPoem(models.Model):
      AuthorName = models.CharField(max_length=50)

      Type = models.CharField(max_length=10)

      Title = models.CharField(max_length=100)

      Content = models.CharField(max_length=1000)



