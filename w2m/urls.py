from django.urls import path
from .views import *

urlpatterns = [
    path("users/", UserList.as_view()),
    path("user/delete/<pk>/", UserDelete.as_view()),
    path("user/<pk>/", UserDetail.as_view()),
    path("groups/", GroupList.as_view()),
    path("group/<pk>/", GroupDetail.as_view()),
    path("group/update/<pk>/", GroupUpdate.as_view()),
    path("group/delete/<pk>/", GroupDelete.as_view()),
    path("group/image/<pk>/", GroupImage.as_view()),
]
