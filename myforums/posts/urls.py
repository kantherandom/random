from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('posts/',views.posts, name='posts'),
    path('create_post/', views.show_form, name="create_post"),
    path('create_a_post/', views.create_form, name="create_a_post"),
    path('get_post_by_topic/<str:topic>', views.get_post_by_topic, name="get_post_by_topic")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)