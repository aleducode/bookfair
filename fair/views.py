"""Fair Views"""

# Django
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView

# Models
from fair.models import Guest, Post, Program, Topic

class IndexView(TemplateView):
    """Fair index"""
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        kwargs.setdefault('view', self)
        kwargs['guests'] = Guest.objects.all()
        kwargs['notices'] = Post.objects.all().order_by('-created')
        kwargs['programs'] = Program.objects.all().order_by('-created')
        kwargs['topics'] = Topic.objects.all()
        if self.extra_context is not None:
            kwargs.update(self.extra_context)
        return kwargs

class NoticeDetailView(DetailView):
    """Notice detail"""
    template_name='notice-detail.html'
    pk_url_kwarg = 'pk'
    queryset=Post.objects.all()
    context_object_name='notice'

    def get_context_data(self, **kwargs):
        """Insert the form into the context dict."""
        if 'form' not in kwargs:
            kwargs['notices'] = Post.objects.all().exclude(
                pk=self.object.pk).order_by('-created')
        return super().get_context_data(**kwargs)

class SoonView(TemplateView):
    """SoonView index"""
    template_name = 'base/soon.html'