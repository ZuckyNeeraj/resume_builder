from django.db import models

# Create your models here.


class UserData(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    phone_num = models.CharField(max_length=15)
    city = models.CharField(max_length=20)
    desc = models.TextField(max_length=500)
    tenthSchoolName = models.CharField(max_length=30)
    twelveSchoolName = models.CharField(max_length=30)
    collegeName = models.CharField(max_length=30)
    tenthPercentage = models.CharField(max_length=30)
    twelvePercentage = models.CharField(max_length=30)
    collegePercentage = models.CharField(max_length=30)
    projectName = models.CharField(max_length=30)
    projectDesc = models.TextField(max_length=500)
    firstSkill = models.CharField(max_length=30)
    secondSkill = models.CharField(max_length=30)
    thirdSkill = models.CharField(max_length=30)
    firstAchievement = models.CharField(max_length=30)
    secondAchievement = models.CharField(max_length=30)
    thirdAchievement = models.CharField(max_length=30)
    hobby = models.CharField(max_length=50)



