from core.contants import MEDIUM_TEXT_LENGTH
from core.models import BaseModel
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

USER = get_user_model()

# Create your models here.
class Profile(
    BaseModel
):

    name = models.CharField(
        verbose_name=_("User name"),
        max_length=MEDIUM_TEXT_LENGTH,
        help_text=_("user name , can't be blank")
    )

    description = models.CharField(
        verbose_name=_("User description"),
        max_length=MEDIUM_TEXT_LENGTH,
        blank=True
    )

    about = models.TextField(
        verbose_name=_("About user"),
        blank=True,
        null=False,
        help_text=_("About user text , can be blank")
    )

    photo = models.ImageField(
        verbose_name=_("User profile photo"),
        upload_to="users/profile/image/%Y/%m/",
        blank=True,
        null=True
    )

    contact_email = models.CharField(
        verbose_name=_("User contact email"),
        max_length=MEDIUM_TEXT_LENGTH,
        blank=True
    )

    contact_phone_number = models.CharField(
        verbose_name=_("User contact phone number"),
        max_length=13,
        blank=True,
    )

    user = models.OneToOneField(
        verbose_name=_("User onwer of profile"),
        to=USER,
        on_delete=models.CASCADE,
        related_name="profile"
    )

    def __str__(self):
        return f"{self.user.username} - profile"

    class Meta:
        db_table = "profile"
        verbose_name = _("User Profile")
        verbose_name_plural = _("Users Profiles")
        ordering = ['created_at']
