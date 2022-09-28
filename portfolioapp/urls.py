from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="api-overview"),
    path("about-me/",views.aboutMe,name="aboutMe"),
    path("personal-skills/",views.personalSkills,name="personal-skills"),
    path("professional-skills/",views.professionalSkills,name="professional-skills"),
    path("education/",views.education,name="education"),
    path("tools/",views.tools,name="tools"),
    path("portfolio/",views.portfolio,name="portfolio"),
    path("contact-me/",views.contactMe,name="contactMe"),
    
]
