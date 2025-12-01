"""Sort a list of people and set targets"""

from person import Person
import random

class TargetSorter:
    """Sorting class"""

    def __init__(self, people: list[Person]) -> None:
        self.people: list[Person] = people

    def get_targets(self) -> None:
        """Assings targets for list of people"""
        targets: list[Person] = self.people.copy()
        for person in self.people:
            target: Person = random.choice(targets)
            while target.name == person.name:
                target = random.choice(targets)
            targets.remove(target)
            person.set_target(target.name)
