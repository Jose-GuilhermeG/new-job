from django.urls import path
from rest_framework.routers import SimpleRouter

from job import views

router = SimpleRouter()
router.register(
    "jobs",
    views.JobOpeningViewSet,
    basename='job-opening'
)

urlpatterns = [
    path(
        'skills/',
        views.SkillListCreateView.as_view(),
        name="skils"
    )
]

urlpatterns += router.urls