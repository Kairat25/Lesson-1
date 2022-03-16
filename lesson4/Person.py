from package import models, config
from db import db
if config.staging:

    person = []


    for person in config.fake_db:
        person.append(
            models.Person(person['username'], person['salary'].info())
        )
        print(person)

else:

    while True:
        username = input('Username: ')
        salary = int(input('Salary'))
        person = models.Person(username, salary)
        db.append(person)
        print(db)

