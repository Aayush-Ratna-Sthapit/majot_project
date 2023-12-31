from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Profile(models.Model):
    POSITION_CHOICES = (
        ('admin', 'admin'),
        ('manager', 'manager'),
        ('employee', 'employee'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES,null=True,blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.EmailField(blank=True,null=True)
    photo = models.ImageField(null=True,blank=True)
    bio = models.TextField(null=True,blank=True)

    def __str__(self):
        return str(self.name)


'''@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        # Check if a profile with the same user already exists
        profile, _ = Profile.objects.get_or_create(user=instance)
        profile.name = instance.username
        profile.save()
    else:
        # If the User instance already existed, you can update the related Profile here.
        instance.profile.name = instance.username
        instance.profile.save()'''
        

class Project(models.Model):
    name = models.CharField(max_length=200,null=False,blank=False)
    description = models.TextField(null=False,blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-date_created']

    
class Task(models.Model):
    TODO="TO DO"
    COMPLETED='COMPLETED'
    INPROGRESS='IN-PROGRESS'
    STATUS_CHOICES = [
        (TODO, 'TO DO'),
        (COMPLETED, 'COMPLETED'),
        (INPROGRESS, 'IN-PROGRESS'),
        ]
    
    title = models.CharField(max_length=150)
    description = models.TextField(null=True,blank=True)
    project = models.ForeignKey(Project,null=True,blank=True, on_delete=models.CASCADE)
    assignee = models.ForeignKey(Profile, null=True,blank=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(null=True,blank=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES,null=True,blank=True,default= TODO)
    

    def __str__(self):
        return self.title
 
