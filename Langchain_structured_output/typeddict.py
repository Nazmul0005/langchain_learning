from typing import TypeDict
class Person(TypedDict):
    name: str
    age: int

new_person: Person = {'name': 'Rakib', 'age': 234}

print(new_person)