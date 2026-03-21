from core.contants import MEDIUM_TEXT_LENGTH
from core.models import BaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
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
