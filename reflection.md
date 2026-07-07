# PawPal+ Project Reflection

## 1. System Design

Three core actions that the user should be able to do are see the daily schedule, add information about themselves and their pet, and add new care activities for their pets. 

**a. Initial design**

- Briefly describe your initial UML design.
My initial UML design has 4 classes, which are called Task, Owner, Pet, and Scheduler. Each class had its own attributes and methods with some of the classes being related to each other. For example, the Pet class would get from the Task class. 

- What classes did you include, and what responsibilities did you assign to each?
I included 4 classes, which were Pet, Owner, Task, and Scheduler. The Task class has attributes that describe the task and its status in terms of time, and there are methods to get the attributes. The Owner class has attributes that are information about them and methods to edit the pets they have. The Pet class also has attributes with information about them, but they also have methods to edit the tasks they have. The Scheduler class has an attribute with the list of the pets and methods that will sort and filter the tasks depending on the pet. 

**b. Design changes**

- Did your design change during implementation?
Yes, my design did change during implementation. 

- If yes, describe at least one change and why you made it. 
One change I made was to include the Pet class in the Task class as an attribute. I had asked Claude Code what logic bottlenecks there could be. I was told that when the get_all_tasks() method is called in the Scheduler class, it would go through all of the tasks, which could slow down the process. By including the Pet name in the Task class, we could look for the specific Pet name instead, whcih would speed up the process. 

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
One tradeoff the scheduler makes is that it does not check for the overlapping times and instead checks for only exact time matches. For example, if task 1 was from 3:00-3:30, and task 2 was from 3:15-4:00, then the scheduler would say they did not overlap because it is not an exact match. 

- Why is that tradeoff reasonable for this scenario?
This tradeoff is reasonable for this scenario because if the person in charge of task 2 was busy doing task 1, then all of the tasks would not be completed by the time they need to be done. This causes the daily schedule to constantly be pushed back. 

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
