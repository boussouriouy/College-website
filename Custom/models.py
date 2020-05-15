from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length = 60)
    img = models.ImageField(upload_to='image')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    
#def get_absolute_url(self):
    #return reverse("Custom:tableau ", kwargs={"pk": self.pk})

