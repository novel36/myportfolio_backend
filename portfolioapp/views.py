from asyncio import tasks
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from portfolioapp.models import Task,AboutME,Education,Tools,Portfolio,ContactMe
from .serializers import *
from .models import Task

@api_view(['GET'])
def index(request):
    api_urls={
        "About Me":'/about-me/',
        "Education":'/education/',
        "Tools":'/tools/',
        "Portfolio":'/portfolio/',
        "Contact Me":'/contact-me/',
        "Personal Skills":'/personal-skills/',
        "Professional Skills":'/professional-skills/',
        "SocialMedia Links":'/socialmedia-links/',
    }
    return Response(api_urls)

@api_view(['GET'])
def aboutMe(request):
    aboutMe=AboutME.objects.all()
    serializer=AboutMeSerializer(aboutMe, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def personalSkills(request):
    personalskills=PersonalSkill.objects.all()
    serializer=PersonalSkillSerializer(personalskills, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def professionalSkills(request):
    professionalskills=ProfessionalSkill.objects.all()
    serializer=ProfessionalSkillSerializer(professionalskills, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def education(request):
    education=Education.objects.all()
    serializer=EducationSerializer(education, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def tools(request):
    tools=Tools.objects.all()
    serializer=ToolsSerializer(tools, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def portfolio(request):
    portfolio=Portfolio.objects.all()
    serializer=PortfolioSerializer(portfolio, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def socialmediaLinks(request):
    socialMediaLink=SocialmediaLinks.objects.all()
    serializer=SocialmediaLinksSerializer(socialMediaLink, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def contactMe(request):
    serializer=ContactMeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    # contactMe=ContactMe.objects.all()
    # serializer=ContactMeSerializer(contactMe, many=True)
    return Response(serializer.data)