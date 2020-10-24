import random
import psycopg2

# connect to database
conn = psycopg2.connect(
    host="localhost",
    database="Practice",
    user="postgres",
    password="none")
cursor = conn.cursor()

# get a list of all the students
cursor.execute("SELECT * FROM students")
studentList = cursor.fetchall()

# get a list of all courses
cursor.execute("select * FROM courses")
courseList = cursor.fetchall()

# loop over all students
for student in studentList:
    for course in courseList:
        # takes a course by chance to randomize data
        if random.randint(0, 100) < 33:
            cursor.execute("INSERT INTO tookCourse(f_student_id, f_course_id) VALUES("
                           + str(student[1]) + ", '" + str(course[0]) + "')")

# commit and close connection
cursor.close()
conn.commit()
conn.close()