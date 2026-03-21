from job.filters import SkillFilter
from job.models import Skill
from job.serializers import SkillSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class SkillListCreateView(
    ListCreateAPIView
):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = SkillFilter
