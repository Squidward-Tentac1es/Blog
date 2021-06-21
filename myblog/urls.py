from django.urls import path
from django.conf.urls import url


from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
    BlogCommentView,
    SignUpView,
    ActivateAccount
)


urlpatterns = [
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/comment/', BlogCommentView.as_view(), name='post_comment'),
    path('', BlogListView.as_view(), name='home'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
]

