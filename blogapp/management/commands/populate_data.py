from typing import Any
from blogapp.models import Post,Catogery
from django.core.management.base import BaseCommand
import random





class Command(BaseCommand):
    help = "This commends inserts post data"

    def handle(self, *args, **options: Any):
        # deleting existing data
        Post.objects.all()

        title = [
    "The feature of AI",
    "Climate change solutions",
    "Remote work Trends",
    "Quantam compiting explained",
    "Renewable enrgy Innovations",
    "Deep leaning demystified",
    "Post-pandemic economic outlook",
    "Block chain in Finance",
    "Story telling in marketting",
    "Medical Technology advaces",
    "Space exploration challengs ",
    "Psychology of Decision making",
    "Evolution of Social media",
    "The art of cooking",
    "Cultural diversity in society",
    "Sustainable Development investment",
    "Globalization impact",
    "Power of mindfullness",
    "online learning revolution",
    "Art and technology fusion"
]

        content = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod te",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod te",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod te",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod te",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod te",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod te",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod te",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod te",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod te",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod te",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod te",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod te",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod te",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod te",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod te",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod te",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod te",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod te",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod te",
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod te",

]
        
        img_url = [

    "https://picsum.photos/id/1/800/400",
    "https://picsum.photos/id/2/800/400",
    "https://picsum.photos/id/3/800/400",
    "https://picsum.photos/id/4/800/400",
    "https://picsum.photos/id/5/800/400",
    "https://picsum.photos/id/6/800/400",
    "https://picsum.photos/id/7/800/400",
    "https://picsum.photos/id/8/800/400",
    "https://picsum.photos/id/9/800/400",
    "https://picsum.photos/id/10/800/400",
    "https://picsum.photos/id/11/800/400",
    "https://picsum.photos/id/12/800/400",
    "https://picsum.photos/id/13/800/400",
    "https://picsum.photos/id/14/800/400",
    "https://picsum.photos/id/15/800/400",
    "https://picsum.photos/id/16/800/400",
    "https://picsum.photos/id/17/800/400",
    "https://picsum.photos/id/18/800/400",
    "https://picsum.photos/id/19/800/400",
    "https://picsum.photos/id/20/800/400",
]
        
        catogries = Catogery.objects.all()
        
        for title,content,img_url in zip(title,content,img_url):
            Category = random.choice(catogries)
            Post.objects.create(title=title,content=content,img_url=img_url,Category=Category)
        
        self.stdout.write(self.style.SUCCESS("Completed inserting data!"))