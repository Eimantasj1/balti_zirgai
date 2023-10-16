from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField
from django.urls import reverse

User = get_user_model()

class Type(models.Model):
    name = models.CharField(max_length=20, unique=True)
    detail = models.CharField(max_length=1000, blank=True)
    
    class Meta:
        verbose_name = _("type")
        verbose_name_plural = _("types")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("type_detail", kwargs={"pk": self.pk})

class Beer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    qty = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    detail = models.CharField(max_length=1000, blank=True)
    beer_type = models.ForeignKey(
        Type, verbose_name=_('beer type'),
        on_delete=models.CASCADE,
        related_name="beer"
        )
    drinker = models.ForeignKey(
        User, verbose_name=_("drinker"), 
        on_delete=models.CASCADE,
        null=True, blank=True
        )
    
    class Meta:
        verbose_name = _("beer")
        verbose_name_plural = _("beers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("beer_detail", kwargs={"pk": self.pk})
    

order_status =(
    (0, _("pending")),
    (1, _("in progres")),
    (2, _("completed")),
    (3, _("canceled")),
)


class Order(models.Model):
    date = models.DateTimeField(_("date"), auto_now=False, auto_now_add=True)
    qty = models.IntegerField(blank=False)
    status = models.PositiveIntegerField(_("status"), choices=order_status, default=0)
    beer = models.ForeignKey(
        Type, verbose_name=_('ordered beer'),
        on_delete=models.CASCADE,
        related_name="order"
    )
    

    class Meta:
        verbose_name = _("order")
        verbose_name_plural = _("orders")

    def __str__(self):
        return f'{self.id}, {self.date}, {self.get_status_display()}'

    def get_absolute_url(self):
        return reverse("order_detail", kwargs={"pk": self.pk})





    


