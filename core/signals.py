from django.dispatch import receiver
from django.db.models.signals import post_save

from core.models import *


@receiver(post_save, sender=Statement)
def create_quote(sender, instance, created, **kwargs):
    if created and instance.statement_type == 'Quote':
        Quotation.objects.create(statement=instance)
