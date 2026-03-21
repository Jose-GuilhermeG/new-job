import django_filters as filters
from job.models import Skill


class SkillFilter(
    filters.FilterSet
):
    name = filters.CharFilter(field_name="name",lookup_expr="icontains")

    class Meta:
        model = Skill
        fields = ["name"]
