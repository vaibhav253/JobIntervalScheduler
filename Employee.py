import DBconnection
from DBconnection import connection
import sys
import JobScheduler
import time





def main():
    menu()
    choice = int(input('Enter your choice'))
    while choice!=5:
        if choice == 1:
            DBconnection.connection()
            cur = connection.db.cursor()

            # Use all the SQL you like
            cur.execute("SELECT * FROM employee")

            # print all the first cell of all the rows
            for row in cur.fetchall():
                Emp = [row[0], row[1], row[2]]
                # print(Emp)
            # print (row[2])
                print(Emp)
            sys.exit()
        elif choice == 2:
            DBconnection.connection()
            cur = connection.db.cursor()
            id = input('Enter Employee id = ')
            name = input('Enter Employee name = ')
            Hours = input('Enter Hours that can Employee Works = ')

            #val = (name, Hours)
            sql = "INSERT INTO employee (idemployee,employeename, hours) VALUES (%s, %s,%s)"
            val = (id,name,Hours )
            cur.execute(sql, val)

            connection.db.commit()
            # print all the first cell of all the rows
            cur.execute("SELECT * FROM employee")
            for row in cur.fetchall():
                Emp = [row[0], row[1], row[2]]
                # print(Emp)
                # print (row[2])
                print(Emp)
            sys.exit()
        elif choice == 3:
            #print(JobScheduler.Assign(),"are assigned for job.")
            Jobtime = int(input("Enter the time of job in seconds:"))
            JobScheduler.Assign()
            #print(JobScheduler.Assign(),"are busy in other job.")
            for i in range(Jobtime):
                #print(i)
                time.sleep(1)
            print("job finish")
            print("all employees are free now.")
            sys.exit()
        elif choice ==4:
            sys.exit()
        else:
           print ("Invalid Choice")
           sys.exit()

        menu()
        choice = input('Enter your choice = ')

def menu():
    #Choices
    print ('Choose your Option below')
    print ("Employee Details = 1")
    print ('Add new Employee Details = 2')
    print ('Assign a Job = 3')
    print ('Quit the program = 4')

if __name__ == '__main__':
    main()