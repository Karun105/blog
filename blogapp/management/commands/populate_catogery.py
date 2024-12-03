from typing import Any
from blogapp.models import Catogery
from django.core.management.base import BaseCommand





class Command(BaseCommand):
    help = "This commends inserts post data"

    def handle(self, *args, **options):

        Catogery.objects.all().delete()

        catogries = ['Sports','Technology','Science','Art','Food']
        
        for catogery_name in catogries:
            Catogery.objects.create(name = catogery_name)
        
        self.stdout.write(self.style.SUCCESS("Completed inserting data!"))