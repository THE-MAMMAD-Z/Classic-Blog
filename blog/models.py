from django.db import models

class Post(models.Model) :
    title=models.CharField(max_length=225)
    category=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image/')
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    content=models.TextField()
    autor=models.CharField(max_length=100)

    def call_the_post(self):
        txt1 = "My name is {fname}, Im {age}".format(fname = self.title , age = 36)
        return txt1

    def __str__(self):
        return self.title
    

class Todo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    priority = models.IntegerField(default=1)
    is_done  = models.BooleanField()

    class Meta():
        db_table = "todos"


