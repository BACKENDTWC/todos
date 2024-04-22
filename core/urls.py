from django.urls import path
from core import views

urlpatterns = [
    path("",views.index),
    path("todos/",views.my_todos),
    path("todos/<id>/mark/",views.mark_todo),
    path("todos/create/",views.create_todo),
    path("display/",views.display),
    path("create-teacher/",views.create_teacher),
    path("view-teachers/",views.get_teachers),
    path("profile/",views.ProfileView.as_view()),
]