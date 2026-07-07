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
    task1 = Task(id="Task1", description="Go on a walk", due_date_time=now.replace(hour=9,minute=0), frequency="Daily", status="In-Progress", is_completed=False)
    task2 = Task(id="Task2", description="Feed bird food", due_date_time=now.replace(hour=12,minute=0), frequency="Daily", status="In-Progress", is_completed=False)
    task3 = Task(id="Task3", description="Wash dog", due_date_time=now.replace(hour=14, minute=0), frequency="Weekly", status="In-Progress", is_completed=False)

    # Add the correct tasks to the respective pets
    dog.add_task(task1)
    bird.add_task(task2)
    dog.add_task(task3)

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


if __name__ == "__main__":
    main()