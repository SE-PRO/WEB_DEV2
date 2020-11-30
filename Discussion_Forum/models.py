from django.db import models 
from django.utils import timezone   
#parent model
class forum(models.Model):
    name=models.CharField(max_length=200,default="anonymous")
    topic= models.CharField(max_length=300)
    description = models.TextField(max_length=1000,blank=True)
    date_created=models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return str(self.topic)


    
 
#child model 1
class Discussion(models.Model):
    forum = models.ForeignKey(forum,blank=True,on_delete=models.CASCADE)
    discuss = models.TextField(max_length=1000)
  
      
    def __str__(self):
        return str(self.forum)
