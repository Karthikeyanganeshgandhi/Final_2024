from django.db import models

# class bench(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.IntegerField()
#     description = models.TextField()
#     image = models.ImageField(upload_to='images/')

#     def __str__(self):
#         return self.name

class contactdetail(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=170)
    website=models.URLField(max_length=200, blank=True, null=True)
    comment=models.TextField()

    def __str__(self):
        return self.name


