from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
class TestReport(models.Model):

    Age=models.IntegerField(default=1,validators=[MaxValueValidator(102),MinValueValidator(0)])
    HR=models.FloatField(default=0)
    O2Sat=models.FloatField(default=0)
    Temp=models.FloatField(default=0)
    SBP=models.FloatField(default=0)
    DBP=models.FloatField(default=0)
    Resp=models.FloatField(default=0)
    MAP=models.FloatField(default=0)