"""Fair Urls"""

#Django
from django.urls import path

#Views
from fair import views

urlpatterns = [
    path(
        route='',
        view=views.IndexView.as_view(),
        name='index'
        ),
    path(
        route='noticia/<int:pk>',
        view=views.NoticeDetailView.as_view(),
        name='notice'
        ),
]
