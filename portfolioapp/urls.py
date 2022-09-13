from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="api-overview"),
    path("about-me/",views.aboutMe,name="aboutMe"),
    path("skills/",views.skills,name="skills"),
    path("education/",views.education,name="education"),
    path("tools/",views.tools,name="tools"),
    path("Portfolio/",views.portfolio,name="Portfolio"),
    path("contactme/",views.contactMe,name="contactMe"),
    
]
