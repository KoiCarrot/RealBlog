from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.PostDetailView.as_view(),name = 'detail'),
    url(r'^category/(?P<pk>[0-9]+)/$',views.CategoryView.as_view(),name = 'category'),
]