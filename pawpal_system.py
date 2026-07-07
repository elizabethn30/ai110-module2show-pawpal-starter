from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class Owner:
    name: str
    id: str
    pets: List['Pet'] = field(default_factory=list)

    def add_pet(self, pet: 'Pet') -> None:
        """Add a pet to the owner's list of pets."""
        self.pets.append(pet)

    def remove_pet(self, pet: 'Pet') -> None:
        """Remove a pet from the owner's list of pets."""
        if pet in self.pets:
            self.pets.remove(pet)

    def get_pets(self) -> List['Pet']:
        """Return the list of pets owned by this owner."""
        return self.pets


@dataclass
class Pet:
    name: str
    id: str
    owner: Owner
    tasks: List['Task'] = field(default_factory=list)

    def add_task(self, task: 'Task') -> None:
        """Add a task to the pet's task list."""
        task.pet = self
        self.tasks.append(task)

    def remove_task(self, task: 'Task') -> None:
        """Remove a task from the pet's task list."""
        if task in self.tasks:
            self.tasks.remove(task)
            task.pet = None

    def get_tasks(self) -> List['Task']:
        """Return the list of tasks assigned to this pet."""
        return self.tasks

    def get_task_by_id(self, task_id: str) -> 'Task':
        """Return a specific task by its ID, or None if not found."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def get_owner(self) -> Owner:
        """Return the owner of this pet."""
        return self.owner


@dataclass
class Task:
    id: str
    description: str
    due_date_time: datetime
    frequency: str
    status: str
    is_completed: bool
    pet: Pet = None

    def update_status(self, new_status: str) -> None:
        """Update the task's status to a new value."""
        self.status = new_status

    def mark_complete(self) -> None:
        """Mark the task as completed."""
        self.is_completed = True
        self.status = "completed"

    def get_description(self) -> str:
        """Return the task's description."""
        return self.description

    def get_due_date_time(self) -> datetime:
        """Return the task's due date and time."""
        return self.due_date_time


class Scheduler:
    def __init__(self, pets: List[Pet] = None):
        self.pets = pets if pets is not None else []

    def add_pet(self, pet: Pet) -> None:
        """Add a pet to the scheduler's list of pets."""
        self.pets.append(pet)

    def remove_pet(self, pet: Pet) -> None:
        """Remove a pet from the scheduler's list of pets."""
        if pet in self.pets:
            self.pets.remove(pet)

    def get_all_tasks(self) -> List[Task]:
        """Return all tasks across all pets in the scheduler."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks

    def get_tasks_by_status(self, status: str) -> List[Task]:
        """Return all tasks with a specific status across all pets."""
        tasks = []
        for pet in self.pets:
            for task in pet.get_tasks():
                if task.status == status:
                    tasks.append(task)
        return tasks

    def get_overdue_tasks(self) -> List[Task]:
        """Return all incomplete tasks that are past their due date."""
        overdue_tasks = []
        current_time = datetime.now()
        for pet in self.pets:
            for task in pet.get_tasks():
                if task.due_date_time < current_time and not task.is_completed:
                    overdue_tasks.append(task)
        return overdue_tasks

    def get_tasks_for_pet(self, pet: Pet) -> List[Task]:
        """Return all tasks assigned to a specific pet."""
        return pet.get_tasks()
