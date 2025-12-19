from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    complete = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def status(self):
        today = date.today()

        # type: ignore[attr-defined]
        
        if self.complete:
            return "Complete"
        
        if self.due_date:
            days_diff = (self.due_date - today).days

            if days_diff < 0:
                return f"Overdue by {-days_diff} Day(s)"
            elif days_diff == 0:
                return f"Due Today"
            elif days_diff == 1:
                return f"Due Tomorrow"
            elif days_diff <= 3:
                return f"Due in {days_diff} Days"
            elif days_diff <= 7:
                return f"Due this week"
            else:
                return "No Rushhh"
        return "No Deadline"



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    display_name = models.CharField(max_length = 100, blank=True)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(
        upload_to= 'profile_pics/',
        default = 'profile_pics/default_profile.png',
        blank=True
    )

    def __str__(self):
        return self.user.username
    
