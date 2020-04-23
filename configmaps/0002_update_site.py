# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-06-04 16:05
from __future__ import unicode_literals

from django.db import migrations
from django.conf import settings
#import socket
import os

SITES = {
    'old': {
        'domain': 'example.com',
        'name': 'example.com',
    },
    'new': {
        'domain': os.environ['DJANGO_ALLOWED_HOSTS'],
        'name': os.environ['DJANGO_ALLOWED_HOSTS'].partition('.')[2],
    },
}

def update_site(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')

    # Get or create our new site:
    #   If all migrations are being run at once, there shouldn't be any sites
    #     since the initial example site is created by a post_migrate signal
    #   If this is being run individually, then we overwrite the existing
    #     example.com site
    site, created = Site.objects.get_or_create(id=settings.SITE_ID)

    # Update with new site name and domain
    site.name = SITES['new']['name']
    site.domain = SITES['new']['domain']
    site.save()


def revert_site(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')

    # Get current site matching SITE_ID should be ligo.org
    site = Site.objects.get(id=settings.SITE_ID)

    # Revert to original site
    site.name = SITES['old']['name']
    site.domain = SITES['old']['domain']
    site.save()


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(update_site, revert_site),
    ]
