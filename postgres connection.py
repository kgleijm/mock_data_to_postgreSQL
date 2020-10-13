import random
import string  # gives us easy access to an alphabetic list of uppercase characters
import psycopg2  # handles postgreSQL connection
import names  # spits out random names

print(names.get_full_name())
# get list of all chars not represented in our database
listOfChars = list(string.ascii_uppercase)
# create a list to store our tuples representing persons
listOfPersons = list()
for character in listOfChars:
    while True:
        gender = random.choice(('male', 'female'))
        # loop over names until name with a satisfying
        # first character has been found
        name = names.get_full_name(gender)
        # generate tuple of relevant information
        if name[0] == character:
            listOfPersons.append((
                name.split(' ')[0],                 # first name
                name.split(' ')[1],                 # last name
                'M' if gender == 'male' else 'F',   # gender
                random.randint(16, 26)              # age
            ))
            break
    print(listOfPersons[-1])

# connect to the database
conn = psycopg2.connect(
    host="localhost",
    database="Practice",
    user="postgres",
    password="none")
cursor = conn.cursor()

for person in listOfPersons:
    cursor.execute("insert into students(firstname, lastname, studentgender, studentage) " +
                "VALUES ('" + person[0] + "', '" + person[1] + "', '" + person[2] + "', " + str(person[3]) + ")")

# commit and close connection
cursor.close()
conn.commit()
conn.close()

