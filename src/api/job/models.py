from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from core.contants import MEDIUM_TEXT_LENGTH , LONG_TEXT_LENGTH
from core.models import BaseModel
from job.enums import JobLocation , JobType
from job.utils import jobs_curriculum_path

USER = get_user_model()

# Create your models here.
class JobOpening(
    BaseModel
):
    title = models.CharField(
        verbose_name=_("Job Opening Title"),
        max_length=LONG_TEXT_LENGTH,
        null=False,
        blank=False,
    )
    
    description = models.TextField(
        verbose_name=_("Job Opening Description"),
        blank=False,
        null=False,
    )
    
    start_at = models.DateTimeField(
        verbose_name=_("Job Opening Start Date"),
        null=False,
        blank=False,
    )
    
    finish_at = models.DateTimeField(
        verbose_name=_("Job Opening Finish Date"),
        null=False,
        blank=False,
    )
    
    
    skills = models.ManyToManyField(
        verbose_name=_("Job Opening Skills"),
        to="Skill",
        related_name="job_openings"
    )
    
    type = models.CharField(
        verbose_name=_("Job type"),
        blank=False,
        null=False,
        choices=JobType.choices,
        default=JobType.FULL_TIME,
        max_length=10
    )
    
    location = models.CharField(
        verbose_name=_("Job location"),
        blank=False,
        null=False,
        choices=JobLocation.choices,
        default=JobLocation.ON_SITE,
        max_length=10
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        db_table = "job_opening"
        verbose_name = _("Job Opening")
        verbose_name_plural = _("Job Openings")
        ordering = ['-created_at']

class Skill(
    BaseModel
):

    name = models.CharField(
        verbose_name=_("Skill name"),
        max_length=MEDIUM_TEXT_LENGTH,
        unique=True,
        blank=False,
        null=False,
    )

    slug = models.SlugField(
        verbose_name=_("Skill slug"),
        max_length=MEDIUM_TEXT_LENGTH,
        unique=True,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "skill"
        verbose_name = _("Skill")
        verbose_name_plural = _("Skills")
        ordering = ['-name']

class JobEnrollment(
    BaseModel
):
    job = models.ForeignKey(
        verbose_name=_("Job"),
        to=JobOpening,
        on_delete=models.CASCADE,
        related_name="enrollments",
        blank=False,
        null=False
    )
    
    user = models.ForeignKey(
        verbose_name=_("User onwer of enrollment"),
        to=USER,
        on_delete=models.CASCADE,
        related_name="enrollments",
        blank=False,
        null=False
    )
    
    contact_email = models.EmailField(
        verbose_name=_("User contact email"),
        max_length=MEDIUM_TEXT_LENGTH,
        blank=False,
        null=False,
    )
    
    curriculum = models.FileField(
        verbose_name=_("User Curriculum"),
        blank=False,
        upload_to=jobs_curriculum_path
    )
    
    def __str__(self):
        return f"{self.job.title} - {self.user.username}"
    
    class Meta:
        db_table = "job_enrollments"
        verbose_name = _("job enrollment")
        verbose_name_plural = _("jobs enrollments")
        ordering = ["-created_at"]
        unique_together = ["job" , "user"]