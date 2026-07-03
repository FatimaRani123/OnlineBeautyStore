from django.core.management.base import BaseCommand
from orders.services import archive_old_orders

class Command(BaseCommand):
    help = 'Move orders older than 2 days to archived status.'

    def handle(self, *args, **options):
        archive_old_orders()
        self.stdout.write(self.style.SUCCESS('Archived orders older than 2 days.'))
