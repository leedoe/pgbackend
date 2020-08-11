import json
import pprint
import environ
import os
import sys
from pathlib import Path

import django
from django.conf import settings

PROJECT_ROOT = Path(os.path.realpath(__file__)).parent.parent
sys.path.append(os.path.dirname(PROJECT_ROOT))
# print(sys.path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pgbackend.settings.local")
env = environ.Env()

# settings.configure(default_settings=env('DJANGO_SETTINGS_MODULE'), DEBUG=True)
django.setup()

from items.models import Item
from users.models import User

with open('./items/crawling/items.json', 'r', encoding='utf8') as fp:
    items = json.load(fp)

item_instances = []
for item in items:
    if len(item['title']) > 150:
        print(item['title'])
    item_instances.append(Item(
        name=item['title'],
        thumbnail=item['image'],
        price=item['price'],
        link=item['link'],
        soldout=item['soldout'],
        store_name=item['homepage']
    ))

Item.objects.bulk_create(item_instances)
    