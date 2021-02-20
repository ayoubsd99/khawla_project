from django.db import models

# Create your models here.



class BaseModel(models.Model):
    reference=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now=False, auto_now_add=True)
    deleted=models.BooleanField(default=False)
    

    class Meta:
        abstract=True

    def __str__(self):
        return self.reference

 
    