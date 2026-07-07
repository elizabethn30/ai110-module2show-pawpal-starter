from datetime import datetime
from pawpal_system import Owner, Pet, Task, Scheduler

def main():
    now = datetime.now()

    # Create the owner
    owner = Owner(name="Sarah", id="Owner1")

    # Create at least two pets with the Pet class
    dog = Pet(name="Bill", id="Dog1", owner=owner)
    bird = Pet(name="Joan", id="Bird1", owner=owner)
    
    # Create at least three tasks with different times
    task1 = Task(id="Task1", description="Go on a walk", due_date_time=now.replace(hour=9,minute=0), frequency="daily", status="In-Progress", is_completed=False)
    task2 = Task(id="Task2", description="Feed bird food", due_date_time=now.replace(hour=12,minute=0), frequency="daily", status="In-Progress", is_completed=False)
    task3 = Task(id="Task3", description="Wash dog", due_date_time=now.replace(hour=14, minute=0), frequency="weekly", status="In-Progress", is_completed=False)
    
    # Phase 4 Step 2: Add out of order tasks
    task4 = Task(id="Task4", description="Wash", due_date_time=now.replace(hour=10, minute=0), frequency="weekly", status="In-Progress", is_completed=False)
    task5 = Task(id="Task5", description="Walk around park", due_date_time=now.replace(hour=13, minute=0), frequency="daily", status="In-Progress", is_completed=False)

    # Phase 4 Step 4: Add tasks occurring at the same time
    task6 = Task(id="Task6", description="Clean bird cage", due_date_time=now.replace(hour=15, minute=0), frequency="daily", status="In-Progress", is_completed=False)
    task7 = Task(id="Task7", description="Nap time", due_date_time=now.replace(hour=15, minute=0), frequency="daily", status="In-Progress", is_completed=False)

    # Add the correct tasks to the respective pets
    dog.add_task(task1)
    bird.add_task(task2)
    dog.add_task(task3)
    bird.add_task(task4)
    dog.add_task(task5)
    bird.add_task(task6)
    dog.add_task(task7)

    # Adds pets to the correct owner
    owner.add_pet(dog)
    owner.add_pet(bird)

    # Print "Today's Schedule" to the terminal
    scheduler = Scheduler([dog, bird])
    print("Today's Schedule: ")
    print()
    all_pet_tasks = scheduler.get_all_tasks()
    for task in all_pet_tasks:
        print(f"Task: {task.description}")
        print(f"  Pet: {task.pet.name}")
        print(f"  Time: {task.due_date_time}")
        print(f"  Frequency: {task.frequency}")
        print(f"  Status: {task.status}")
        print()

    # Using sort_by_time() method
    print("Sorting method:")
    sorted_tasks = scheduler.sort_by_time()
    for task in sorted_tasks:
        print(f"{task.due_date_time} {task.description}")
    print()

    print("Filter method:")
    incomplete_tasks = scheduler.filter_tasks(is_completed=False)
    for task in incomplete_tasks:
        print(f"{task.description}")
    print()

    print("Conflict Detection:")
    conflicts = scheduler.check_conflicts()
    if conflicts:
        for conflict in conflicts:
            print(conflict)
    else:
        print("No conflicts found")
    print()


if __name__ == "__main__":
    main()