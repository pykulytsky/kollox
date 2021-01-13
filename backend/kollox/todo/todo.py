from .models import (
    Project,
    SimpleToDoList,
    ToDoItem,
    Reminder
)

from typing import Optional, Union

from authentication.models import User

class TodoListCreator:
    def __init__(self) -> None:
        raise NotImplementedError


class TodoItemCreator:
    def __init__(self,
                title: str,
                owner: User,
                todo_list: Union[SimpleToDoList, Project],
                as_subtask: Optional[bool] = False,
                parent_task: Optional[ToDoItem] = None,
                reminder: Optional[Reminder] = None,
                ) -> None:
        
        if reminder:
            self.remind_me = True
            self.create_reminder()
        raise NotImplementedError

    def create_reminder(self):
        

