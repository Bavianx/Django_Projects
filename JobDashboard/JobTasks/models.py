from django.db import models

class Appcontent(models.Model):
    title = models.CharField(max_length=50)
    salary = models.FloatField()
    location = models.CharField(max_length=25)
    date = models.DateField(null = True, blank=True)  #Allows the field to be omitted in forms and the database to store a null value until inputted


    def __str__(self):
        return f"{self.title}: {self.salary} : {self.location}"