from django.db import models

class Post(models.Model) :
    title=models.CharField(max_length=225)
    category=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image/')
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    content=models.TextField()
    autor=models.CharField(max_length=100)


    def __str__(self):
        return self.title