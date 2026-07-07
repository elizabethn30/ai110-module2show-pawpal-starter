from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Task:
    description: str
    due_date_time: datetime
    status: str
    is_completed: bool

    def update_status(self, new_status: str) -> None:
        pass

    def get_description(self) -> str:
        pass

    def get_due_date_time(self) -> datetime:
        pass


@dataclass
class Pet:
    name: str
    id: str
    owner: 'Owner'
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task) -> None:
        pass

    def remove_task(self, task: Task) -> None:
        pass

    def get_tasks(self) -> List[Task]:
        pass

    def get_owner(self) -> 'Owner':
        pass


@dataclass
class Owner:
    name: str
    id: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet) -> None:
        pass

    def remove_pet(self, pet: Pet) -> None:
        pass

    def get_pets(self) -> List[Pet]:
        pass


class Schedule:
    def __init__(self, pets: List[Pet] = None):
        self.pets = pets if pets is not None else []

    def add_pet(self, pet: Pet) -> None:
        pass

    def remove_pet(self, pet: Pet) -> None:
        pass

    def get_all_tasks(self) -> List[Task]:
        pass

    def get_tasks_by_status(self, status: str) -> List[Task]:
        pass

    def get_overdue_tasks(self) -> List[Task]:
        pass

    def get_tasks_for_pet(self, pet: Pet) -> List[Task]:
        pass
