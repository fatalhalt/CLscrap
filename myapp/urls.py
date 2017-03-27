from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.app, name='app'),        # at this point /app string is consumed
    url(r'^page/', views.page, name='page'),  # at this point /app string is consumed as well, therefore /app/page hits this
]