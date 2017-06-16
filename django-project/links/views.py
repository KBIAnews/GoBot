# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from bakery.views import BuildableListView, BuildableDetailView

from django.shortcuts import render

from .models import Link

# Create your views here.

class LinkDetailView(BuildableDetailView):
    model = Link
    template_name = 'links/link_detail.html'

    def get_object(self):
        if self.kwargs['slug']:
            return Link.objects.get(short_link=self.kwargs['slug'])
        return super(LinkDetailView, self).get_object()