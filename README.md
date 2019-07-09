# Stack-Assignment
Implement a native stack using any language of your choice.
A stacks is a data structures that make it easy to insert, delete and search for particular items. It allow access to only one data item, the last item inserted. If you remove this item, you can access the next-to-last item inserted, and so on.

Suppose interested applicants for School of Computational Intelligence (SCI), 2019 Graduate Trainee Progam are to submit their CVs to the company email for review by the Human Resource team before further call up for interview. It may happen that when it is time to review the applications, the hiring team can chose to go through the CVs the way it appeared in their mail box, that is starting from the last-in applicant. This is a typical stack example since it is going to be a Last-In-First-Out (LIFO) mechanism.

To implement this, let us now create a Python stack that allow the user to perform push and pop operations by calling the method of the class.
This is the runtime cases of the program
push <name>
pop
stop
Which action do you want to perform?: push Fidelis
['push', 'Fidelis']
push <name>
pop
stop
Which action do you want to perform?: push Francis
['push', 'Francis']
push <name>
pop
stop
Which action do you want to perform?: push Kenneth
['push', 'Kenneth']
push <name>
pop
stop
Which action do you want to perform?: pop
['pop']
Popped name:  Kenneth
push <name>
pop
stop
Which action do you want to perform?: pop
['pop']
Popped name:  Francis
push <name>
pop
stop
Which action do you want to perform?: pop
['pop']
Popped name:  Fidelis
push <name>
pop
stop
Which action do you want to perform?: pop
['pop']
Cannot pop, stack is empty.
push <name>
pop
stop
Which action do you want to perform?: stop
['stop']

Process finished with exit code 0

                      Explanation
The above runtime cases is a clear demonstration of how the company is going to review the applicants CVs suppose only three persons applied. They will start with the last applicant, Kenneth, then to Francis and finally Fidelis the first applicant.
