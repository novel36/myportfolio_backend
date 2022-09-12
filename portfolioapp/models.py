from django.db import models


# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)

    def __str__(self):
        return self.title




class MySkill(models.Model):
    skillname=models.CharField(max_length=100)

class AboutME(models.model):
    name=models.CharField(max_length=50)
    # skill=
    # socialmediaLinks=
    photo1=models.ImageField()
    photo2=models.ImageField()

class Tools(models.Model):
    tool_name=models.CharField(max_length=200)
    used_for=models.CharField(max_length=500)

class SocialmediaLinks(models.Model):
    socialMediaName=models.CharField(max_length=150)
    link=models.CharField(max_length=500)

class ContactMe(models.Model):
    firstname=models.CharField(max_length=300)
    lasname=models.CharField(max_length=300)

class Skills(models.Model):
    # professionalSkill=
    # personalSkill=
    name=models.CharField()

class ProfessionalSkill(models.Model):
    skillname=models.CharField(max_length=700)
    skill_in_percent=models.IntegerField(max_length=150)

class PersonalSkill(models.Model):
    skillname=models.CharField(max_length=700)
    skill_in_percent=models.IntegerField(max_length=150)

class Education(models.Model):
    schoolName=models.CharField(max_length=500)
    level_of_school=models.CharField()
    started_year=models.CharField()
    finished_year=models.CharField()

class Portfolio(models.Model):
    project_title=models.CharField()
    project_type=models.CharField()
    project_images=models.CharField()
    project_link=models.CharField()