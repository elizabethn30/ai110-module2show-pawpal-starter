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
The scheduler considers the time and the frequency of the task. 

- How did you decide which constraints mattered most?
I decided which constraints mattered the most with what would be the most convenient for the user. For example, frequency is automatically done by the Scheduler class when it is marked complete on the schedule

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
One tradeoff the scheduler makes is that it does not check for the overlapping times and instead checks for only exact time matches. For example, if task 1 was from 3:00-3:30, and task 2 was from 3:15-4:00, then the scheduler would say they did not overlap because it is not an exact match. 

- Why is that tradeoff reasonable for this scenario?
This tradeoff is reasonable for this scenario because if the person in charge of task 2 was busy doing task 1, then all of the tasks would not be completed by the time they need to be done. This causes the daily schedule to constantly be pushed back. 

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
I used AI to create the UML document, coming up with how to format the methods, debugging, rearranging code blocks around, brainstorming ideas for the methods, and creating the tets cases. 

- What kinds of prompts or questions were most helpful?
The prompts that were most helpful were when I was very specific on what I was asking. If my prompts were not specific, then I found that the AI would get confused and do something unrelated to what I was asking. 

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
One moment where I did not accept an AI suggestion as-is was when I was working on the original schedule output in main.py, and the AI tried to overcomplicate the schedule by sorting by time before I got to that Phase. The AI suggestion was to use the sorted() function inside main.py, but I saw that later on I would use the sorted() function in a method in the Scheduler class. I did not accept the AI suggestion because it was too complicated for what I wanted at the moment. 

- How did you evaluate or verify what the AI suggested?
I evaluated what the AI suggested by looking at the next Phases, and I saw that I did not need to make my current schedule output sorted by time. 

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
I tested if daily/weekly recurrences were properly added, tests were in the correct order, conflicts were correctly identified, and the edge cases for each of the sorting and filtering methods. 

- Why were these tests important?
These tests were important to make sure that what I implemented were able to be used. The edge cases were important to make sure the methods work all the time, not just sometimes. 

**b. Confidence**

- How confident are you that your scheduler works correctly?
I am about 4/5 confident that the scheduler works correctly. 

- What edge cases would you test next if you had more time?
I would test more on how the scheduler would work whenever there is an empty input for an attribute. For example, I would have an edge case for when there is no description for the task. 

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
I was most satisfied that I learned how important a UML diagram can be to a project. 

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?
I would improve the schedule output. 

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
One important thing I learned about designing systems is that there is a lot of tinkering to go through before the final product. 