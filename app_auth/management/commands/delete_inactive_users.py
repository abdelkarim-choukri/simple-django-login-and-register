from django.conf import settings
from django.utils import timezone
from django.core.management.base import BaseCommand

from datetime import timedelta
from app_auth.models import User

class Command(BaseCommand):
    help = 'Delete inactive user accounts'

    def handle(self, *args, **options):
        User.objects.filter(
            is_active=False,
            date_joined__lt=timezone.now() - timedelta(days=settings.ACCOUNT_ACTIVATION_DAYS)
        ).delete()
