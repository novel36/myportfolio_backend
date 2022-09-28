
from django.db import models


# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.title



class AboutME(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=2000,default="")
    photo1=models.ImageField(upload_to="ProfileImages",)
    photo2=models.ImageField(upload_to="ProfileImages",)

    class Meta:
        verbose_name_plural = "AboutME"

    def __str__(self):
        return self.name

class MySkill(models.Model):
    skillname=models.CharField(max_length=100)
    aboutme= models.ForeignKey(AboutME, on_delete=models.CASCADE,null=True)
    class Meta:
        verbose_name_plural = "MySkills"

    def __str__(self):
        return self.skillname

class SocialmediaLinks(models.Model):
    socialMediaName=models.CharField(max_length=150)
    link=models.CharField(max_length=500)
    aboutme= models.ForeignKey(AboutME, on_delete=models.CASCADE,null=True)


    class Meta:
        verbose_name_plural = "SocialmediaLinks"

    def __str__(self):
        return self.socialMediaName


class PersonalSkill(models.Model):
    skillname=models.CharField(max_length=700)
    skill_in_percent=models.IntegerField()

    class Meta:
        verbose_name_plural = "PersonalSkills"

    def __str__(self):
        return self.skillname

class ProfessionalSkill(models.Model):
    skillname=models.CharField(max_length=700)
    skill_in_percent=models.IntegerField()


    class Meta:
        verbose_name_plural = "ProfessionalSkills"

    def __str__(self):
        return self.skillname



class Education(models.Model):
    schoolName=models.CharField(max_length=500)
    level_of_school=models.CharField(max_length=150)
    started_year=models.CharField(max_length=150)
    finished_year=models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Education"

    def __str__(self):
        return self.schoolName

class Portfolio(models.Model):
    project_title=models.CharField(max_length=150)
    project_type=models.CharField(max_length=150)
    project_images=models.ImageField(upload_to="PortfolioImages",)
    project_link=models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Portfolio"

    def __str__(self):
        return self.project_title

class Tools(models.Model):
    tool_name=models.CharField(max_length=200)
    used_for=models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "Tools"

    def __str__(self):
        return self.tool_name


class ContactMe(models.Model):
    firstname=models.CharField(max_length=300)
    lastname=models.CharField(max_length=300)
    email=models.EmailField(max_length=70,blank=True,unique=True)
    message=models.TextField()

    class Meta:
        verbose_name_plural = "ContactMe"

    def __str__(self):
        return self.firstname

