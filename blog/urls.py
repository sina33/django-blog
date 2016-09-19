from django.conf.urls import url, include

from blog import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^posts/$', view=views.PostList.as_view()),
    url(r'^post/(?P<pk>[0-9]+)/$', view=views.PostDetail.as_view()),
    url(r'^post/', view=views.PostCreate.as_view()),
    # url('^', include('django.contrib.auth.urls')),
]
