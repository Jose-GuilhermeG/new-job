import django_filters as filters
from job.models import JobOpening, Skill


class SkillFilter(
    filters.FilterSet
):
    name = filters.CharFilter(field_name="name",lookup_expr="icontains")

    class Meta:
        model = Skill
        fields = ["name"]

class JobFilter(
    filters.FilterSet
):

    class Meta:
        model = JobOpening
        fields = ["skills","type","location"]
