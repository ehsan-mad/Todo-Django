from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    STATUS= (
        ('pending' , 'Pending'),
        ('completed' , 'Completed'),
        
    )
    CATEGORY = (
        ('general', 'General'),
        ('work', 'Work'),
        ('others', 'Others'),

    )
    title= models.CharField(max_length=100)
    description= models.TextField()
    due_date=models.DateField()
    due_time=models.TimeField()
    status= models.CharField(max_length=20, default='pending', choices=STATUS)
    category=models.CharField(max_length=50, default='general', choices=CATEGORY)
    is_completed=models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
