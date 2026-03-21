from django.urls import path

from job import views

urlpatterns = [
    path(
        'skills/',
        views.SkillListCreateView.as_view(),
        name="skils"
    )    
]
