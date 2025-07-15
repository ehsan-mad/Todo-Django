from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.task_list, name="task_list"),
    path("taskCreate/", views.task_create, name="task_create"),
    path("taskUpdate/<int:task_id>/", views.task_update, name="task_update"),
    path("taskDelete/<int:task_id>/", views.task_delete, name="task_delete"),
    path("taskComplete/<int:task_id>/", views.task_complete, name="task_complete"),
    path("register/", views.register, name="register"),
    path(
        "login/",
        LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),
]
