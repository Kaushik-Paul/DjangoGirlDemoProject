from rest_framework.urls import path

from . import views


urlpatterns = [
    path('post-list/', views.PostListGenericView.as_view(), name='post_list_api'),
    path('post-list/<str:pk>', views.PostDetailGenericView.as_view(), name='post_detail_api'),

]

