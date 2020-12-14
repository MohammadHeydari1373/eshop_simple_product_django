from django.db import models

# Create your models here.
import os ,random
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
def filename_ext(filepath) :
    basename = os.path.basename(filepath)
    name , ext = os.path.split(basename)
    return  name , ext
def file_upload(instance , filename) :
    newname = random.randint(1,27665456)
    name , ext = filename_ext(filename)
    final_name = f"{instance.id}-{instance.title}{ext}"
    return f'products/{newname}/{final_name}'

class ProductManager(models.Manager):

    def get_featured(self):
        return self.get_queryset().filter(featured=True)


    def get_by_id(self , productId):
        qs = self.get_queryset().filter(id = productId)
        if qs.count()==1 :

            return qs.first()
        else:
            return None
class Product(models.Model) :
    title = models.CharField(max_length=200)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=20 , decimal_places=2)
    image = models.ImageField(upload_to=file_upload , blank=True , null=True)
    featured = models.BooleanField(default = False)
    objects = ProductManager()
    timestamp = models.DateTimeField(auto_now_add=True)
    def get_url_slug(self):
        return f"{self.slug}"
    def __str__(self):
        return self.title

def product_pre_save_reciver(sender , instance , *args , **kwargs) :
    if not instance.slug :
        instance.slug = unique_slug_generator(instance)
pre_save.connect(product_pre_save_reciver,sender=Product)