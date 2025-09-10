#Task1:

list1 = []
len1 = int(input("Enter length of first list: "))
for i in range(len1):
    num1 = int(input("Enter number: "))
    list1.append(num1)
list2 = []
len2 = int(input("Enter length of second list: "))
for j in range(len2):
    num2 = int(input("Enter number: "))
    list2.append(num2)

merged_list = list1 + list2
merged_list.sort()

print("Merged and Sorted List:", merged_list)

#Task2:
list1 = []
len1 = int(input("Enter length of first list: "))
for i in range(len1):
    num1 = int(input("Enter number: "))
    list1.append(num1)

list2 = []
len2 = int(input("Enter length of second list: "))
for j in range(len2):
    num2 = int(input("Enter number: "))
    list2.append(num2)

merged_list = list1 + list2
merged_list.sort()

print("Merged and Sorted List:", merged_list)

print("Smallest element:", min(merged_list))
print("Largest element:", max(merged_list))

#Task3:
birthdays = {
    "Albert Einstein": "03/14/1879",
    "Benjamin Franklin": "01/17/1706",
    "Ada Lovelace": "12/10/1815"
}

print("Welcome to the birthday dictionary. We know the birthdays of:")
for name in birthdays:
    print(name)

name = input("Who's birthday do you want to look up? ")

if name in birthdays:
    print(f"{name}'s birthday is {birthdays[name]}.")
    print(name,"'s birthday is ", (birthdays[name]))
else:
    print("Sorry, we don't have the birthday information for that person.")

#Task4:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}
keys = ["name", "salary"]
new_dict = {k: sample_dict[k] for k in keys}

print("New Dictionary:", new_dict)