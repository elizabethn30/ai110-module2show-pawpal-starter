from datetime import datetime, timedelta
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


# --- SORTING CORRECTNESS ---

def test_sort_tasks_chronologically():
    """Tasks should be ordered by earliest due date first."""
    owner = Owner(name="Owner", id="O1")
    pet = Pet(name="Bill", id="P1", owner=owner)
    now = datetime.now()

    task_morning = Task(id="T1", description="Morning walk", due_date_time=now.replace(hour=8, minute=0), frequency="daily", status="In-Progress", is_completed=False)
    task_afternoon = Task(id="T2", description="Afternoon play", due_date_time=now.replace(hour=14, minute=0), frequency="daily", status="In-Progress", is_completed=False)
    task_evening = Task(id="T3", description="Evening dinner", due_date_time=now.replace(hour=18, minute=0), frequency="daily", status="In-Progress", is_completed=False)

    # Add in random order
    pet.add_task(task_afternoon)
    pet.add_task(task_evening)
    pet.add_task(task_morning)

    scheduler = Scheduler([pet])
    sorted_tasks = scheduler.sort_by_time()

    # Verify chronological order
    assert sorted_tasks[0].id == "T1"
    assert sorted_tasks[1].id == "T2"
    assert sorted_tasks[2].id == "T3"
    assert sorted_tasks[0].due_date_time < sorted_tasks[1].due_date_time < sorted_tasks[2].due_date_time


def test_sort_empty_list():
    """Sorting with no tasks should return empty list."""
    scheduler = Scheduler([])
    assert scheduler.sort_by_time() == []


def test_sort_same_time_handling():
    """Tasks at identical times should be handled without error."""
    owner = Owner(name="Owner", id="O1")
    pet = Pet(name="Bill", id="P1", owner=owner)
    now = datetime.now()

    task1 = Task(id="T1", description="Task A", due_date_time=now, frequency="daily", status="In-Progress", is_completed=False)
    task2 = Task(id="T2", description="Task B", due_date_time=now, frequency="daily", status="In-Progress", is_completed=False)

    pet.add_task(task1)
    pet.add_task(task2)

    scheduler = Scheduler([pet])
    sorted_tasks = scheduler.sort_by_time()

    assert len(sorted_tasks) == 2
    assert sorted_tasks[0].due_date_time == sorted_tasks[1].due_date_time


# --- RECURRENCE LOGIC ---

def test_daily_task_creates_next_occurrence():
    """Completing a daily task should create a new task scheduled for the next day."""
    owner = Owner(name="Owner", id="O1")
    pet = Pet(name="Bill", id="P1", owner=owner)
    base_time = datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)

    task = Task(
        id="T1",
        description="Daily walk",
        due_date_time=base_time,
        frequency="daily",
        status="In-Progress",
        is_completed=False
    )
    pet.add_task(task)

    task.mark_complete()

    # Verify original task is marked complete
    assert task.is_completed == True
    assert task.status == "completed"

    # Verify new task was created for the next day
    next_task = pet.get_task_by_id("T1_next")
    assert next_task is not None
    assert next_task.is_completed == False
    assert next_task.status == "In-Progress"
    assert next_task.due_date_time == base_time + timedelta(days=1)


def test_weekly_task_creates_next_occurrence():
    """Completing a weekly task should create a new task scheduled for one week later."""
    owner = Owner(name="Owner", id="O1")
    pet = Pet(name="Bill", id="P1", owner=owner)
    base_time = datetime.now().replace(hour=10, minute=0, second=0, microsecond=0)

    task = Task(
        id="T2",
        description="Weekly bath",
        due_date_time=base_time,
        frequency="weekly",
        status="In-Progress",
        is_completed=False
    )
    pet.add_task(task)

    task.mark_complete()

    # Verify new task was created for 7 days later
    next_task = pet.get_task_by_id("T2_next")
    assert next_task is not None
    assert next_task.due_date_time == base_time + timedelta(days=7)
    assert next_task.frequency == "weekly"


def test_one_time_task_no_recurrence():
    """Completing a one-time task should not create another occurrence."""
    owner = Owner(name="Owner", id="O1")
    pet = Pet(name="Bill", id="P1", owner=owner)
    now = datetime.now()

    task = Task(
        id="T3",
        description="Vet appointment",
        due_date_time=now,
        frequency="once",
        status="In-Progress",
        is_completed=False
    )
    pet.add_task(task)

    initial_count = len(pet.get_tasks())
    task.mark_complete()

    # Should not create a next task
    assert len(pet.get_tasks()) == initial_count
    assert pet.get_task_by_id("T3_next") is None


# --- CONFLICT DETECTION ---

def test_detects_overlapping_task_times():
    """Scheduler should identify when multiple tasks are scheduled at the exact same time."""
    owner = Owner(name="Owner", id="O1")
    pet = Pet(name="Bill", id="P1", owner=owner)
    now = datetime.now()

    task1 = Task(id="T1", description="Clean cage", due_date_time=now.replace(hour=15, minute=0), frequency="daily", status="In-Progress", is_completed=False)
    task2 = Task(id="T2", description="Nap time", due_date_time=now.replace(hour=15, minute=0), frequency="daily", status="In-Progress", is_completed=False)

    pet.add_task(task1)
    pet.add_task(task2)

    scheduler = Scheduler([pet])
    conflicts = scheduler.check_conflicts()

    # Should have at least one conflict
    assert len(conflicts) > 0
    assert any("Conflict" in msg for msg in conflicts)


def test_multiple_conflicts_same_slot():
    """Multiple tasks at the same time should generate multiple conflict warnings."""
    owner = Owner(name="Owner", id="O1")
    pet = Pet(name="Bill", id="P1", owner=owner)
    now = datetime.now()

    task1 = Task(id="T1", description="Task A", due_date_time=now, frequency="daily", status="In-Progress", is_completed=False)
    task2 = Task(id="T2", description="Task B", due_date_time=now, frequency="daily", status="In-Progress", is_completed=False)
    task3 = Task(id="T3", description="Task C", due_date_time=now, frequency="daily", status="In-Progress", is_completed=False)

    pet.add_task(task1)
    pet.add_task(task2)
    pet.add_task(task3)

    scheduler = Scheduler([pet])
    conflicts = scheduler.check_conflicts()

    # 3 tasks at same time = 3 pairwise conflicts: (T1,T2), (T1,T3), (T2,T3)
    assert len(conflicts) == 3


def test_conflicts_empty_scheduler():
    """Empty scheduler should report no conflicts."""
    scheduler = Scheduler([])
    conflicts = scheduler.check_conflicts()
    assert conflicts == []
