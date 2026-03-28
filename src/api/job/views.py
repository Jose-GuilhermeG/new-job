from core.mixins import (
    ViewSetAddPermissionPerActionMixin,
    ViewSetGetSerializerClassMixin,
)
from django.shortcuts import get_object_or_404
from job.filters import JobFilter, SkillFilter
from job.models import JobOpening, Skill
from job.permissions import isJobEnrollmentOwner
from job.serializers import (
    JobEnrollmentSerializer,
    JobOpeningCreateUpdateSerializer,
    JobOpeningDetailSerializer,
    JobOpeningListSerializer,
    SkillSerializer,
)
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


# Create your views here.
class SkillListCreateView(
    ListCreateAPIView
):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = SkillFilter

class JobOpeningViewSet(
    ViewSetGetSerializerClassMixin,
    ModelViewSet,
):
    queryset = JobOpening.objects.all()
    serializer_class = JobOpeningCreateUpdateSerializer
    serializers_class_per_action = {
        "list" : JobOpeningListSerializer,
        "create" : JobOpeningCreateUpdateSerializer,
        "retrieve" : JobOpeningDetailSerializer
    }

class JobEnrollmetViewSet(
    ViewSetAddPermissionPerActionMixin,
    ModelViewSet
):

    serializer_class = JobEnrollmentSerializer
    permission_classes = [IsAuthenticated]
    permission_per_action = {
        'retrieve' : isJobEnrollmentOwner,
        'destroy' : isJobEnrollmentOwner,
        'partial_update' : isJobEnrollmentOwner,
        'update' : isJobEnrollmentOwner
    }

    def get_job(self) :
        job_id = self.kwargs.get("job_id" , None)
        return get_object_or_404(JobOpening , pk = job_id)

    def get_queryset(self):
        return self.get_job().enrollments.select_related("user", "user__profile").prefetch_related("user__profile__skills", "job__skills")

    def perform_create(self, serializer):
        serializer.save(user = self.request.user , job = self.get_job())

class JobSearchView(
    ListAPIView
):
    serializer_class = JobOpeningListSerializer
    filterset_class = JobFilter

    def get_queryset(self):
        query = self.kwargs.get("q")
        return JobOpening.objects.search(query)
