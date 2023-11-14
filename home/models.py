from django.db import models

from wagtail.models import Page, LockableMixin
from wagtail.snippets.models import register_snippet


class HomePage(Page):
    pass


@register_snippet
class Teaser(LockableMixin, models.Model):
    body = models.CharField(max_length=255)
