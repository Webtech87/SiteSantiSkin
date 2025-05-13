from importlib.metadata import requires

from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Dr(models.Model):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email address"), blank=True, unique=True)
    is_staff = models.BooleanField(
        _("staff status"),
        default=True,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    dr_license = models.CharField(
        _("dr license"),
        max_length=150,
        blank=True,
        unique=True,
        help_text=_(
            "dr_license -> already exists."
        ),
    )

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
