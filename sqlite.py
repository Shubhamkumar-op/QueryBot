import sqlite3
connection=sqlite3.connect("student.db")
cursor=connection.cursor()
table_info="""
create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT)
"""

cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('Alice','Data Science','B',78)''')
cursor.execute('''Insert Into STUDENT values('Bob','Data Science','A',92)''')
cursor.execute('''Insert Into STUDENT values('Charlie','Data Science','C',65)''')
cursor.execute('''Insert Into STUDENT values('David','DEVOPS','B',70)''')
cursor.execute('''Insert Into STUDENT values('Eve','DEVOPS','C',58)''')
cursor.execute('''Insert Into STUDENT values('Fay','DEVOPS','A',80)''')
cursor.execute('''Insert Into STUDENT values('Grace','Machine Learning','B',88)''')
cursor.execute('''Insert Into STUDENT values('Hannah','Machine Learning','A',95)''')
cursor.execute('''Insert Into STUDENT values('Ivy','Machine Learning','C',60)''')
cursor.execute('''Insert Into STUDENT values('Jack','Cyber Security','A',85)''')
cursor.execute('''Insert Into STUDENT values('Liam','Cyber Security','B',78)''')
cursor.execute('''Insert Into STUDENT values('Mia','Cyber Security','A',90)''')
cursor.execute('''Insert Into STUDENT values('Noah','AI','B',80)''')
cursor.execute('''Insert Into STUDENT values('Olivia','AI','A',93)''')
cursor.execute('''Insert Into STUDENT values('Paul','AI','C',72)''')
cursor.execute('''Insert Into STUDENT values('Quinn','Cloud Computing','B',82)''')
cursor.execute('''Insert Into STUDENT values('Rita','Cloud Computing','A',91)''')
cursor.execute('''Insert Into STUDENT values('Sam','Cloud Computing','C',64)''')



print("The inserted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)


connection.commit()
connection.close()