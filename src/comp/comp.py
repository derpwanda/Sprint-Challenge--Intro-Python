# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]

# print("Starts with D:")
# r = [name for name in humans if (name.name.startswith('D'))]
# print(r)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D:")
a = [(f"{human.name}") for human in humans if human.name[0] == 'D']
# for human in humans:
#     if human.name[0] == "D":
#         a.append(f"{human.name}")
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [(f"{human.name}") for human in humans if human.name[-1] == "e"]
# for human in humans:
#     if human.name[-1] == "e":  # used slice to output last element
#         b.append(f"{human.name}")
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")

letters = ["C","D", "E", "F","G"]
c = [f"{human.name}" for human in humans for letter in letters if human.name[0] == letter]
# for human in humans:
#     for letter in letters:
#         if human.name[0] == letter:
#             c.append(f"{human.name}")
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [human.age + 10 for human in humans]
# for human in humans:
#     d.append(human.age + 10)
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = [f"{human.name}-{human.age}" for human in humans]
# for human in humans:
#     e.append(f"{human.name}-{human.age}")
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
print("Names and ages between 27 and 32:")
f = [(human.name, human.age) for human in humans if human.age in range(27,33)]
# for human in humans:
#     if human.age in range(27,33):
#         f.append((human.name, human.age))
print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names capitalized and the ages with 5 added to them.
# The "humans" list should be unmodified.
print("All names capitalized:")
g = [Human((human.name.upper()), (human.age + 5)) for human in humans]
# for human in humans:
#     g.append(Human((human.name.upper()), (human.age + 5)))
print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = [math.sqrt(human.age) for human in humans]
# for human in humans:
#     h.append(math.sqrt(human.age))
print(h)
