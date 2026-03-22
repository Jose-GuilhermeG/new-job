from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from job.filters import SkillFilter
from job.models import Skill , JobOpening
from job.serializers import SkillSerializer , JobOpeningListSerializer , JobOpeningCreateUpdateSerializer , JobOpeningDetailSerializer
from core.mixins import ViewSetGetSerializerClassMixin

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