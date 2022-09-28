from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="api-overview"),
    path("about-me/",views.aboutMe,name="aboutMe"),
    path("personalskills/",views.personalSkills,name="personalSkills"),
    path("professionalskills/",views.professionalSkills,name="professionalSkills"),
    path("education/",views.education,name="education"),
    path("tools/",views.tools,name="tools"),
    path("portfolio/",views.portfolio,name="portfolio"),
    path("contactme/",views.contactMe,name="contactMe"),
    
]
