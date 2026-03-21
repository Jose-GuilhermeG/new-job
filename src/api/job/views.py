from rest_framework.generics import ListCreateAPIView , RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from job.models import Skill
from job.serializers import SkillSerializer
from job.filters import SkillFilter

# Create your views here.
class SkillListCreateView(
    ListCreateAPIView
):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    permission_classes = [IsAuthenticated]
    filterset_class = SkillFilter