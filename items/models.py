from django.db import models
from django.contrib.auth.models import AbstractUser


from core.models import BaseModel
from core.views import _grf
# Create your models here.



class Item(BaseModel):
    title=models.CharField(max_length=50)
    big_desc=models.TextField()

    def get_miniature(self):
        image =ItemImage.objects.filter(item=self)[0]
        return image.miniature


    def get_images(self):
        images=[]
        for image in ItemImage.objects.filter(item=self):
            images.append(image)
        return images    

    def __str__(self):
        return self.reference

    def generate(self):
        while True:
            random=_grf(35)
            if Item.objects.filter(reference=random).exists():
                continue
            self.reference=random
            break
        return self.reference
    def save(self, *args, **kwargs):
       if self.pk is None:
           self.generate()

       super(Item, self).save(*args, **kwargs) # Call the real save() method    



class Category(BaseModel):
    label=models.CharField(max_length=50)

    def __str__(self):
        return self.reference

    def generate(self):
        while True:
            random=_grf(35)
            if Category.objects.filter(reference=random).exists():
                continue
            self.reference=random
            break
        return self.reference

    def save(self, *args, **kwargs):
       if self.pk is None:
           self.generate()

       super(Category, self).save(*args, **kwargs) # Call the real save() method    




class ItemImage(BaseModel):
    image=models.TextField()
    item=models.ForeignKey("items.Item",on_delete=models.CASCADE)
    miniature=models.TextField()

    def __str__(self):
        return self.reference

    def generate(self):
        while True:
            random=_grf(35)
            if ItemImage.objects.filter(reference=random).exists():
                continue
            self.reference=random
            break
        return self.reference
    def save(self, *args, **kwargs):
       if self.pk is None:
           self.generate()

       super(ItemImage, self).save(*args, **kwargs) # Call the real save() method    


class User(BaseModel,AbstractUser):

    def __str__(self):
        return self.reference


    def generate(self):
        while True:
            random=_grf(35)
            if User.objects.filter(reference=random).exists():
                continue
            self.reference=random
            break
        return self.reference
    def save(self, *args, **kwargs):
       if self.pk is None:
           self.generate()

       super(User, self).save(*args, **kwargs) # Call the real save() method    

       