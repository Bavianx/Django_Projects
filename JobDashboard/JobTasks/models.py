from django.db import models

class Appcontent(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('r1', 'Round 1'),
        ('r2', 'Round 2'),
        ('r3', 'Round 3'),
        ('r4', 'Round 4'),
        ('final', 'Final Round'),
        ('offer', 'Offer'),
        ('rejected', 'Rejected'),
    ]
    title = models.CharField(max_length=50)
    salary = models.FloatField()
    location = models.CharField(max_length=25)
    date = models.DateField(null = True, blank=True)  #Allows the field to be omitted in forms and the database to store a null value until inputted
    company = models.CharField(max_length=20, default='Unknown')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')

    def __str__(self):
        return f"{self.title}: {self.salary} : {self.location} {self.company}"