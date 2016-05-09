##Phase 2 Report

###Initial Planning###

We defined the scrum master as someone who facilitated the meetings. In addition to creating an agenda beforehand, he was responsible for making sure that the group conversation adhered to the agenda and also to take minutes.

Task size was estimated based on the number of components it required. Since our project involves creating a website, tasks that required both frontend and backend programming would be larger than tasks that only required exclusively one or the other. Also the projected number of methods required to write in order to complete each task contributed to the task’s size.

The team planned to build the core functionality of our application as the MVP for the demo. This revolved around the user story of Rachel, who was trying to find foods that fit her dietary restrictions. 

We planned to achieve this by building a website. This involved breaking our group into three teams which were responsible for building the frontend, logic, and backend (database). For the frontend, we only wanted build a simple interface for the user to interact with. This involves a search bar and options to filter results based on dietary restrictions. For the logic, we only wanted to implement functions that would fetch the filtered results from the database. For the database, we designed only the necessary entities ingredients, meals, and tags (which for now only represent dietary restrictions).


###Sprint Backlog###

The idea that we had for our project is a website that helps people stay healthy while still being able to enjoy the food that they eat. The site offers suggestions for healthy meals for the user and tells the user nutritional facts about these foods so that they can find meals that fit their dietary restrictions.

The goal of our team for this sprint was to build a barebones version of our website that was able to handle two or three of our user stories. We wanted to be able to make food recommendations based on dietary restrictions (user story 3), implement a ‘surprise me’ feature that would return any random food (user story 2), and add a sort feature that could sort the results that we received based on different things (user story 5), i.e. how many steps a meal would take. 

The first thing that needed to be implemented for us to do this was the database for our users and meals (Issue 6). This task was assigned to Alex and he used MongoDB in order to implement this. After this the main part of the site could be implemented. 

The next important part to implement was the search bar and results page, we assigned Roland to work on the backend (Issue 12) for these pages and for Shu to work on the frontend (Issue 9). These features were important to the site because they allowed it to complete its main functions as well as had a part in every user story. The backend was implemented using python and flask, while the frontend was implemented using html and bootstrap.

After we had the most important parts of our websites finished, we needed some extra features. After deciding what we would like to do with the site we realized we would need users for our project so we assigned Ryan to the registration page for users and Julian to the account page. The registration page would allow users to be made by taking in a user and password, then creating a user with this information and store them into the database (Issue 10). The account page on the other hand allows users to see what their password and username is as well as the dietary tags that they had. These tags will be used later on to search for foods that only have these tags on them already (Issue 11).

Finally we planned to add two features that could satisfy two different user stories for our website. The ‘surprise me’ feature was assigned to Toumy to implement and the sort feature was assigned to Seung-gyu to implement. The ‘surprise me’ feature was a button you could click and the site would return a random meal from the database (Issue 7). This was decided to be implemented as a method on the backend for the website and would later be implemented as a usable button. The sort feature is a feature that sorts the results given by the site based on a number of possibilities (Issue 8). For this sprint we decided to just make this part of all results queries rather than something the user could choose after receiving the data and had it sort the results by the number of steps that each meal takes.



###Update Meetings###

Meeting Oct23

Location: Skype Call

Determine scrum roles: 10 min
Scrum Master: Ryan
Testers: Seung-Gyu & Alex

Determine sprint 1 backlog: 3:40 - 4:00

Breakdown tasks for sprint 1 backlog: (issues) 4:00 - 4:30

Assign tasks: 
(Never Completed)

Total Time: 1 hour

Attendance:
Ryan
Roland
Alex
Seung-gyu
Shu

Description: Went over plan for Sprint

---------------------------------------------------

Meeting Oct 24

Location: Skype Call

Fill in people who missed last meeting -- est 20 min
7:05 - 7:15

Finalize sprint 1 backlog features -- est 30 min
7:15 - 7:35

Assign tasks -- est 10 min
7:40 - 8

Total: 1 hour

Attendance:
Roland
Alex
Ryan
Julian
Toumy

Description: Caught up people who missed the last meeting and assigned tasks

----------------------------------------------------

Meeting Oct 28

Location Bahen Centre

Reassign Ryan to another role -- 10 min

Attendance:
Roland
Ryan

Description: After talking with the TA we decided not to make a Registration Page and therefore decided to reassign Ryan to work on the frontend of the results page.

----------------------------------------------------

Meeting Oct 31

Location: Skype Call

Go over progress -- 10 min
7:05 - 7:12

Discuss progress goals -- 20 min
7:12 - 7:35

Go over Sprint2 deliverables -- 30 min (Never covered)
Assign deliverables -- 10 min (Never covered)

Final: Set Time for next meeting to prepare for demo

Total: 1h 10 min

Attendance:
Roland
Alex
Ryan
Toumy
Seung-Gyu
Julian
Shu

Description: Discussed progress and planned out what to have done by end of

-----------------------------------------------------------

Meeting Nov1

Location: Skype Call

Go over progress -- 10 min
Time: 5:05 - 5:20

Make sure site is ready for demo -- 20 min

Time: (Did not cover, instead discussed progress on website development)

Go over deliverables -- 40 min

Time: 5:40 - 6:20

Attendance:
Ryan
Roland
Alex
Shu
Seung-Gyu
Julian
Toumy

Description: Worked on deliverables and discussed progress


###Burndown Chart###

![alt text](https://github.com/csc301-fall-2015/project-team13-L0101/blob/master/doc/phase2/images/burndown.jpg "Burndown Chart")

###Review and Retrospective###

**What Tasks were cut out:**

Creating a registration page. Though a user page is part of the design of our website, we were informed by the TA that a registration page would be a waste of time to demo. Therefore we cut it. 

**What tasks were split:**

Since half of our team have little or no web development experience, we paired those people with others who had more experience. Also since the registration page was cut, the members who were supposed to work on that task were left with nothing to do.

**Decisions that went well:**

Correctly identifying the tasks that were put on this sprint’s backlog. These were necessary features for our product.

Pairing less experienced people with ones who are more experienced. We were able to learn and be productive.

Using Python flask minimized the amount of new stuff that group members with no web dev experience had to learn in order to get themselves into the project.

**Decisions that didn’t go well / What to improve:**

Not enforcing the use of forks for every member. Nothing has come of it yet, but as our codebase gets bigger, it would be great if everyone followed the fork, PR, code review system discussed in class. We will strongly consider this going into phase 3.

Issues with MongoDB and Python versions. Many group members had issues getting MongoDB to run as well as attempting to ensuring that a specific version of Python was running. Should have made the installation methods more clear from the start before code needed testing.


