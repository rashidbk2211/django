# models.py
from django.db import models

class UserProfile(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    birthday = models.DateField()
    location = models.CharField(max_length=100)
    about_me = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.full_name




class Education(models.Model):
    college = models.CharField(max_length=100)
    year = models.CharField(max_length=4)  # You could use IntegerField() if you prefer a numeric input
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.college} ({self.year})"



class Experience(models.Model):
    worked_field = models.CharField(max_length=100)
    year = models.CharField(max_length=4)  # or IntegerField() if you prefer
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.worked_field} ({self.year})"

# models.py


class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.IntegerField(default=50)  # Proficiency level from 0 to 100

    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"

# models.py

class Project(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    description = models.TextField()
    project_link = models.URLField(blank=True, null=True)  # Allows for optional link
    image = models.ImageField(upload_to='portfolio_images/')  # Store images in a dedicated folder

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    photo = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name