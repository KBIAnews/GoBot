# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Link(models.Model):
    short_link = models.SlugField("Link Name",
                                  unique=True,
                                  blank=False,
                                  null=False,
                                  help_text="What comes after the / in the URL. Keep it simple. " +
                                            "Avoid spaces and special characters.")
    destination_url = models.URLField("Destination URL",
                                      max_length=2000,
                                      blank=False,
                                      null=False,
                                      help_text="Where are you taking us? " +
                                                "If it ends with # and then something, " +
                                                "delete the # and everything after it.")
    # Choices for the UTM Medium Field
    MEDIUM_RADIO = 'radio'
    MEDIUM_MAILING = 'mailing'
    MEDIUM_WEB_AD = 'banner'
    MEDIUM_EMAIL = 'email'
    MEDIUM_SOCIAL = 'social'
    MEDIUM_CHOICES = (
        (MEDIUM_RADIO, 'Radio - On Air'),
        (MEDIUM_MAILING, 'Mailing'),
        (MEDIUM_WEB_AD, 'Web Ad'),
        (MEDIUM_EMAIL, 'Email'),
        (MEDIUM_SOCIAL, 'Social'),
    )
    campaign_medium = models.CharField("Primary Link Use",
                                       max_length=140,
                                       blank=True,
                                       null=True,
                                       choices=MEDIUM_CHOICES)

    def __str__(self):
        return "%s" % self.short_link

    def get_absolute_url(self):
        return "/%s/" % self.short_link

    class Meta:
        ordering = ['short_link']
