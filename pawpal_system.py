from dataclasses import dataclass, field
from datetime import datetime, timedelta
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
        """Mark task as completed and auto-create next occurrence for recurring tasks.

        For daily/weekly tasks, uses timedelta to calculate next due date:
        - Daily: adds 1 day to current due_date_time
        - Weekly: adds 7 days to current due_date_time
        Creates new task with same properties and adds it to the same pet.
        """
        self.is_completed = True
        self.status = "completed"

        # Create next occurrence for daily or weekly tasks
        if self.frequency.lower() in ["daily", "weekly"]:
            days_to_add = 1 if self.frequency.lower() == "daily" else 7
            next_due_date = self.due_date_time + timedelta(days=days_to_add)

            # Create new task for next occurrence
            next_task = Task(
                id=f"{self.id}_next",
                description=self.description,
                due_date_time=next_due_date,
                frequency=self.frequency,
                status="In-Progress",
                is_completed=False,
                pet=None
            )

            # Add to the same pet if this task is assigned to one
            if self.pet:
                self.pet.add_task(next_task)

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

    def sort_by_time(self) -> List[Task]:
        """Return all tasks sorted chronologically by due date and time.

        Uses Python's sorted() with a lambda key function to extract due_date_time
        for comparison. Returns tasks in ascending order (earliest first).
        """
        return sorted(self.get_all_tasks(), key=lambda task: task.due_date_time)

    def filter_tasks(self, pet_name: str = None, is_completed: bool = None) -> List[Task]:
        """Filter tasks by pet name and/or completion status using list comprehensions.

        Args:
            pet_name: Filter by pet name (string). Pass None to skip this filter.
            is_completed: Filter by completion status (True/False). Pass None to skip.

        Returns:
            List of tasks matching all specified filters. Filters are applied sequentially.
        """
        tasks = self.get_all_tasks()

        if pet_name is not None:
            tasks = [task for task in tasks if task.pet and task.pet.name == pet_name]

        if is_completed is not None:
            tasks = [task for task in tasks if task.is_completed == is_completed]

        return tasks

    def check_conflicts(self) -> List[str]:
        """Detect scheduling conflicts using nested loop comparison.

        Compares each task pair to find exact time matches (same due_date_time).
        Returns warning messages instead of raising exceptions.

        Returns:
            List of warning messages. Empty list if no conflicts found.
        """
        warnings = []
        all_tasks = self.get_all_tasks()

        # Compare each task with other tasks
        for i in range(len(all_tasks)):
            for j in range(i + 1, len(all_tasks)):
                task1 = all_tasks[i]
                task2 = all_tasks[j]

                # If times match, add warning
                if task1.due_date_time == task2.due_date_time:
                    msg = f"Conflict at {task1.due_date_time}: {task1.description} and {task2.description}"
                    warnings.append(msg)

        return warnings
