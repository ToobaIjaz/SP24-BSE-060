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
