from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=256)
    time = models.DateField(auto_now_add=True)

    def __str__(self): 
        return self.title