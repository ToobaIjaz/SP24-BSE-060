#task 1
"""
list1 = input("Enter numbers for List 1 separated by space: ").split()
list2 = input("Enter numbers for List 2 separated by space: ").split()

for i in range(len(list1)):
    list1[i] = int(list1[i])
for i in range(len(list2)):
    list2[i] = int(list2[i])

list1.extend(list2)
list1.sort()
print("Merged and Sorted List:", list1)
"""
#task 1 without split

list1 = []
size1 = int(input("How many numbers in List 1? "))
for i in range(size1):
    num = int(input("Enter a number: "))
    list1.append(num)

list2 = []
size2 = int(input("How many numbers in List 2? "))
for i in range(size2):
    num = int(input("Enter a number: "))
    list2.append(num)

# Merge and sort
list1.extend(list2)
list1.sort()
print("Merged and Sorted List:", list1)

#task
print("Smallest element:", min(list1))
print("Largest element:", max(list1))

# Task 3: Birthday Dictionary

birthdays = {
    "Albert Einstein": "03/14/1879",
    "Benjamin Franklin": "01/17/1706",
    "Ada Lovelace": "12/10/1815"
}
print("Welcome to the birthday dictionary. We know the birthdays of:")
for name in birthdays:
    print(name)

person = input("Who's birthday do you want to look up? ")

if person in birthdays:
    print(person, "'s birthday is", birthdays[person])
else:
    print("Sorry, we don't have that birthday.")


# Task 4: Extract specific keys from a dictionary

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}

keys = ["name", "salary"]  # Keys we want to extract

new_dict = {}
for k in keys:
    new_dict[k] = sample_dict[k]

print("Extracted Dictionary:", new_dict)
