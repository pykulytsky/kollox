from django.urls import path

from todo.api.views import *

urlpatterns = [
    path('all-todo-lists/<int:user_id>/', AllToDoListAPIView.as_view(), name="all_todo_lists")
]
