from django.urls import path

from .api.views import *

urlpatterns = [
    path('all-todo-lists/', AllToDoListAPIView.as_view(), name="all_todo_lists"),
    path('projects/', ProjectListAPIView.as_view(), name="projects"),
    path('project/<int:id>/', ProjectDetailAPIView.as_view(), name="project"),
    path('simple-todo-lists/', SimpleToDoListListAPIView.as_view(), name="simple-todo-lists"),
    path('simple-todo-list/<int:id>/', SimpleToDoListDetailAPIView.as_view(), name="simple-todo-list"),
    path('todos/', ToDoItemListView.as_view(), name="todo_items_list"),
    path('todo/<int:id>/', ToDoItemDetailView.as_view(), name="todo_item_detail"),
    path('todos/favorite/', FavoriteToDoItemListView.as_view(), name="favorite_todos")
]
