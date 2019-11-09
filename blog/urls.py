from django.urls import path
from .views import IndexView, PostDetalle, CreatePostView,PostEditView, PostDeleteView

urlpatterns = [
    path('', IndexView.as_view() , name='home'),
    path('article/<int:pk>/', PostDetalle.as_view() , name='post-detail'),
    path('article/new/', CreatePostView.as_view() , name='post-new'),
    path('article/edit/<int:pk>', PostEditView.as_view() , name='post-edit'),
    path('article/<int:pk>/remove', PostDeleteView.as_view() , name='post-delete'),
    
]