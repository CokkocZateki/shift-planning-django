from django.db import models
import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Employee(models.Model):
    personal_number = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    main_workplace = models.CharField(max_length=50)
    def __str__(self):
        return self.last_name + ', ' + self.first_name

class Workplace(models.Model):
    name = models.CharField(max_length=120)
    workers = models.ManyToManyField(Employee,
            through='Membership')
    DOWNSTAIRS = 'DS'
    UPSTAIRS = 'US'
    AREACHOICES = (
            (DOWNSTAIRS, 'Downstairs'),
            (UPSTAIRS, 'Upstairs'),
            )
    description = models.CharField(
            max_length=30,
            default='None')
    work_area = models.CharField(
            max_length=2,
            choices=AREACHOICES,
            default = DOWNSTAIRS,
            )
    def __str__(self):
        return self.name

class Membership(models.Model):
    worker = models.ForeignKey(Employee,
            on_delete=models.CASCADE)
    workgroup = models.ForeignKey(Workplace,
            on_delete=models.CASCADE)
    date_joined= models.DateField()
    competence = models.IntegerField()

    class Meta:
        ordering = ["competence"]
