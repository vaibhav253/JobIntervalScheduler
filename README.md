# JobIntervalScheduler

A simple Job Assigning program to Employees.

Fatch the employee data from the Mysql server dataset and assign a job to maximum 3 employee according to the emplyee's working hours.

For the mySql connection see the code

[DBconnection.py](https://github.com/vaibhav253/JobIntervalScheduler/blob/master/DBconnection.py)

ExampleDB.csv shows the examples of the employees details.
ExampleDB.csv Data
|idemployee|employeename|hours|
|----------|------------|-----|
|1         |mike        |10   |
|2         |robin       |40   |
|3         |john        |20   |
|4         |kerin       |30   |

Run the only [Employee.py](Employee.py) file for get the menu of choices and from that it will give you a results accoring to that choices.


# Result

After running the Employee.py it will give the results as shown in bleow.
Choose your Option below
Employee Details = 1
Add new Employee Details = 2
Assign a Job = 3
Quit the program = 4
Enter your choice = 

If Choice = 1

result will be

[1, 'mike', 10]

[2, 'robin', 40]

[3, 'john', 20]

[4, 'kerin', 30]


If Choice = 2

it will ask to add new employee detail.

Enter Employee id = 5

Enter Employee name = abc

Enter Hours that can Employee Works = 40



