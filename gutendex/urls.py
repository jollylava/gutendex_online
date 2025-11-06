from django.urls import include, re_path, path
from django.views.generic import TemplateView
from rest_framework import routers

from books import views     # <--- BookViewSet is here
from books.views import proxy    # <--- proxy imported separately


router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)

urlpatterns = [
    re_path(r'^$', TemplateView.as_view(template_name='home.html')),

    # ✅ place proxy BEFORE router include
    path("proxy/", proxy, name="proxy"),

    re_path(r'^', include(router.urls)),
]
