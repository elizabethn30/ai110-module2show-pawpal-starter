from datetime import datetime
from pawpal_system import Owner, Pet, Task, Scheduler


def test_task_completion():
    """Verify that calling mark_complete() changes the task's status."""
    owner = Owner(name="Test Owner", id="O1")
    pet = Pet(name="Test Pet", id="P1", owner=owner)

    task = Task(
        id="T1",
        description="Test task",
        due_date_time=datetime.now(),
        frequency="daily",
        status="pending",
        is_completed=False
    )

    pet.add_task(task)

    # Before marking complete
    assert task.is_completed == False
    assert task.status == "pending"

    # Mark the task as complete
    task.mark_complete()

    # After marking complete
    assert task.is_completed == True
    assert task.status == "completed"


def test_task_addition():
    """Verify that adding a task to a Pet increases that pet's task count."""
    owner = Owner(name="Test Owner", id="O1")
    pet = Pet(name="Test Pet", id="P1", owner=owner)

    # Initial task count should be 0
    assert len(pet.get_tasks()) == 0

    # Create and add a task
    task1 = Task(
        id="T1",
        description="First task",
        due_date_time=datetime.now(),
        frequency="daily",
        status="pending",
        is_completed=False
    )
    pet.add_task(task1)

    # Task count should be 1
    assert len(pet.get_tasks()) == 1

    # Add another task
    task2 = Task(
        id="T2",
        description="Second task",
        due_date_time=datetime.now(),
        frequency="weekly",
        status="pending",
        is_completed=False
    )
    pet.add_task(task2)

    # Task count should be 2
    assert len(pet.get_tasks()) == 2
