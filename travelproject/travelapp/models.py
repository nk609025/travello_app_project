from django.db import models

# Create your models here.
class place(models.Model):
    def __str__(self):
        return self.name
    img=models.ImageField(upload_to='picture')
    name=models.CharField(max_length=100)
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)
