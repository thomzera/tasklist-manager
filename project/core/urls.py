from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import (CustomLoginView, TaskCreate, TaskDelete, TaskDetail,
                    TaskList, TaskUpdate)

urlpatterns = [
    # login e logout
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),

    # crud tasks
    path("", TaskList.as_view(), name="tasks"),
    path("task/<int:pk>/", TaskDetail.as_view(), name="task"),
    path("task-create/", TaskCreate.as_view(), name="task-create"),
    path("task-update/<int:pk>/", TaskUpdate.as_view(), name="task-update"),
    path("task-delete/<int:pk>/", TaskDelete.as_view(), name="task-delete"),
]
