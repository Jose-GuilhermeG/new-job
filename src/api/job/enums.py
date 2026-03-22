from django.db import models
from django.utils.translation import gettext_lazy as _

class JobType(models.TextChoices):
    FULL_TIME = "full_time", _("Full Time")
    PART_TIME = "part_time", _("Part Time")
    INTERNSHIP = "internship", _("Internship")
    
class JobLocation(models.TextChoices):
    ON_SITE = "on_site", _("On Site")
    REMOTE = "remote", _("Remote")
    HYBRID = "hybrid", _("Hybrid")