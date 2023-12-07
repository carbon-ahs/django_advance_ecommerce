from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(_("Name"), max_length=255)

    def __str__(self) -> str:
        return self.name


class Item(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="items"
    )
    name = models.CharField(_("Name"), max_length=255)
    description = models.TextField(_("Description"), blank=True, null=True)
    price = models.FloatField(_("Price(USD)"))
    image = models.ImageField(
        _("Image"), upload_to="item_images", blank=True, null=True
    )
    is_sold = models.BooleanField(_("Sold"), default=False)
    created_by = models.ForeignKey(
        "accounts.CustomUser", verbose_name=_("Created By"), on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
