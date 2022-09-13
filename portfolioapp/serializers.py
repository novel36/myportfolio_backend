from dataclasses import fields
from rest_framework import serializers
from .models import Task,Skills,AboutME,ContactMe,Education,MySkill,PersonalSkill,Portfolio,ProfessionalSkill,SocialmediaLinks,Tools


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Skills
        fields='__all__'

class AboutMeSerializer(serializers.ModelSerializer):
    class Meta:
        model= AboutME
        fields='__all__'

class ContactMeSerializer(serializers.ModelSerializer):
    class Meta:
        model= ContactMe
        fields='__all__'

class MySkillSerializer(serializers.ModelSerializer):
    class Meta:
        model= MySkill
        fields='__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model= Education
        fields='__all__'

class PersonalSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model= PersonalSkill
        fields='__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model= Portfolio
        fields='__all__'

class ProfessionalSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model= ProfessionalSkill
        fields='__all__'

class SocialmediaLinksSerializer(serializers.ModelSerializer):
    class Meta:
        model= SocialmediaLinks
        fields='__all__'

class ToolsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Tools
        fields='__all__'
        