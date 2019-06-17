"""Fair Views"""

# Django
from django.shortcuts import render
from django.views.generic import TemplateView

# Models
from fair.models import Guest, Post

class IndexView(TemplateView):
    """Fair index"""
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        kwargs.setdefault('view', self)
        kwargs['guests'] = Guest.objects.all()
        kwargs['notices'] = Post.objects.all()
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        return kwargs