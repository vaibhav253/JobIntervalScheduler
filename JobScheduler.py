import DBconnection
from DBconnection import connection

#scheduling
def JobScheduler(Emp, Job):

    for i in range(len(Emp)):
        for j in range(len(Emp) - 1 - i):
            if Emp[j][2] < Emp[j + 1][2]:
                Emp[j], Emp[j + 1] = Emp[j + 1], Emp[j]

    # record of free time slots
    result = [False] * Job

    # To store result
    job = ['-1'] * Job

    # find through all given jobs
    for i in range(len(Emp)):

        # Find a free Emp for this job
        for j in range(min(Job - 1, Emp[i][0] - 1), -1, -1):

            # Free Emp found
            if result[j] is False:
                result[j] = True
                job[j] = Emp[i][1]
                break

    # print the assigned job to employees
    print(job)


def Assign():
#mySQL database connection
    DBconnection.connection()
    cur = connection.db.cursor()

# fatching the data from mysql server
    cur.execute("SELECT * FROM employee")
    Emp = list(cur)


    print("Job  assigned to employees")
    JobScheduler(Emp, 3)
    #print(Emp)
# print all the first cell of all the rows
'''for row in cur.fetchall():
    rows = list(cur)
    print(rows)
    Empname = row[1]
    Empno = row[0]
    Hours = row[2]
    #res = list(map(int, str(Hours)))
    #res1 = list(map(int, str(Empno)))
    #print(type(res))
    Emp=[Empname,Empno,Hours]
    #Emp = Emp.tolist()
    print(Emp)

    #print (row[2])
#print(len(Emp))'''
  # Function Call
#Assign()
#connection.db.close()