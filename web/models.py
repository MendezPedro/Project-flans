from django.db import models
import uuid

# Create your models here.
class Flan(models.Model):
    flan_uuid = models.UUIDField()
    name = models.CharField(max_length = 64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()
    precio = models.IntegerField(blank=True, null=True)

    def __str__(self)-> str:
        return self.name
    

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(default = uuid.uuid4, editable = False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length = 64)
    message = models.TextField()

    def __str__(self)-> str:
        return self.customer_email
    

class Review(models.Model):
    flan = models.ForeignKey('Flan', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=100)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user_name} - {self.flan.name}'
