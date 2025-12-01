"""Send emails for secret santa"""

from person import Person
from target import TargetSorter

people: list[Person] = []

with open('emails.txt', 'r') as data:
    emails = data.readlines()
    for email in emails:
        name_email = email.split(',')
        people.append(Person(name_email[0], name_email[1], 'login.txt'))

sorter = TargetSorter(people)
sorter.get_targets()

for person in people:
    person.send_email()
