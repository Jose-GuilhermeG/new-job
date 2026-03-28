from django.urls import path
from job import views
from rest_framework.routers import SimpleRouter

job_enrollment = views.JobEnrollmetViewSet.as_view({"get" : "list" , "post" : "create"})
job_enrollment_detail = views.JobEnrollmetViewSet.as_view({"get" : "retrieve" , "put" : "update" , "patch" : "partial_update" , "delete" : "destroy"})

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
    ),
    path(
        "jobs/<int:job_id>/enrollments/",
        job_enrollment,
        name="job-enrollment"
    ),
    path(
        "jobs/<int:job_id>/enrollments/<int:pk>",
        job_enrollment_detail,
        name="job-enrollment-detail"
    ),
    path(
        "jobs/search/<str:q>/",
        views.JobSearchView.as_view(),
        name="job-search-view"
    )
]

urlpatterns += router.urls
