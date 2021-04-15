from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=20,db_index=True)
    slug = models.SlugField(max_length=20,null=True, blank=True)
    img = models.ImageField(null=True, blank=True, default='placeholder.png', upload_to='profile_pic')
    details = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args,**kwargs):
        self.slug = self.name
        super(Product,self).save(*args,**kwargs)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name



class About(models.Model):
    text = models.TextField(null=True,blank=True)
    ph1 = models.IntegerField(null=True,blank=True)
    ph2 = models.IntegerField(null=True,blank=True)
