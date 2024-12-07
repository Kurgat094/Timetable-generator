from django.db import models

class Teacher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Unit(models.Model):
    name = models.CharField(max_length=100)  # Name of the unit
    code = models.CharField(max_length=10, unique=True)  # Unique code for the unit
    description = models.TextField(blank=True, null=True)  # Optional description
    teacher = models.ForeignKey(
        'Teacher', on_delete=models.SET_NULL, null=True, blank=True, related_name="units"
    )  # Assign a teacher to the unit

    def __str__(self):
        return f"{self.name} ({self.code})"