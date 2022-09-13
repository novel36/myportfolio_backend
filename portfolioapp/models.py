from django.db import models


# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)

    def __str__(self):
        return self.title




class MySkill(models.Model):
    skillname=models.CharField(max_length=100)

    def __str__(self):
        return self.skillname

class SocialmediaLinks(models.Model):
    socialMediaName=models.CharField(max_length=150)
    link=models.CharField(max_length=500)

    def __str__(self):
        return self.socialMediaName

class AboutME(models.Model):
    name=models.CharField(max_length=50)
    mySkill=models.ForeignKey(MySkill,on_delete=models.CASCADE)
    socialmediaLinks=models.ForeignKey(SocialmediaLinks,on_delete=models.CASCADE)
    photo1=models.ImageField()
    photo2=models.ImageField()

    def __str__(self):
        return self.name

class PersonalSkill(models.Model):
    skillname=models.CharField(max_length=700)
    skill_in_percent=models.IntegerField()

    def __str__(self):
        return self.skillname
class ProfessionalSkill(models.Model):
    skillname=models.CharField(max_length=700)
    skill_in_percent=models.IntegerField()

    def __str__(self):
        return self.skillname

class Skills(models.Model):
    professionalSkill=models.ForeignKey(ProfessionalSkill,on_delete=models.CASCADE)
    personalSkill=models.ForeignKey(PersonalSkill,on_delete=models.CASCADE)
    name=models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Education(models.Model):
    schoolName=models.CharField(max_length=500)
    level_of_school=models.CharField(max_length=150)
    started_year=models.CharField(max_length=150)
    finished_year=models.CharField(max_length=150)

    def __str__(self):
        return self.schoolName

class Portfolio(models.Model):
    project_title=models.CharField(max_length=150)
    project_type=models.CharField(max_length=150)
    project_images=models.CharField(max_length=150)
    project_link=models.CharField(max_length=150)

    def __str__(self):
        return self.project_title

class Tools(models.Model):
    tool_name=models.CharField(max_length=200)
    used_for=models.CharField(max_length=500)

    def __str__(self):
        return self.tool_name


class ContactMe(models.Model):
    firstname=models.CharField(max_length=300)
    lasname=models.CharField(max_length=300)

    def __str__(self):
        return self.firstname