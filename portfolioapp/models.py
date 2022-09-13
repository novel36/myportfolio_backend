from django.db import models


# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=200)
    completed=models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.title

class MySkill(models.Model):
    skillname=models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "MySkills"

    def __str__(self):
        return self.skillname

class SocialmediaLinks(models.Model):
    socialMediaName=models.CharField(max_length=150)
    link=models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "SocialmediaLinks"

    def __str__(self):
        return self.socialMediaName

class AboutME(models.Model):
    name=models.CharField(max_length=50)
    mySkill=models.ForeignKey(MySkill,on_delete=models.DO_NOTHING)
    socialmediaLinks=models.ForeignKey(SocialmediaLinks,on_delete=models.DO_NOTHING)
    description=models.CharField(max_length=2000,default="")
    photo1=models.ImageField()
    photo2=models.ImageField()

    class Meta:
        verbose_name_plural = "AboutME"

    def __str__(self):
        return self.name

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

class Skills(models.Model):
    professionalSkill=models.ForeignKey(ProfessionalSkill,on_delete=models.DO_NOTHING)
    personalSkill=models.ForeignKey(PersonalSkill,on_delete=models.DO_NOTHING)
    name=models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.name

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
    project_images=models.CharField(max_length=150)
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
    lasname=models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = "ContactMe"

    def __str__(self):
        return self.firstname