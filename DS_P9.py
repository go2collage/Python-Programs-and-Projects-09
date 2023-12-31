# Python Program / Project

from datetime import datetime

List_A = [
    {'PRN':'x101', 'DOB':'02-03'},
    {'PRN':'x102', 'DOB':'01-12'},
    {'PRN':'x103', 'DOB':'09-01'},
    {'PRN':'x104', 'DOB':'01-05'}
]

# Printing initial List
print("\nList A is: ")
for item in List_A:
    print(item)

# Code to sort List on date
List_A.sort(key= lambda x:datetime.strptime(x['DOB'], '%d-%m'))

print("\nAfter sorting according to DOB is: ")
for item in List_A:
    print(item)

List_B = [
    {'PRN':'x111', 'DOB':'05-10'},
    {'PRN':'x112', 'DOB':'12-02'},
    {'PRN':'x113', 'DOB':'09-09'},
    {'PRN':'x114', 'DOB':'16-05'}
]

# Printing initial List
print("\nList B is: ")
for item in List_B:
    print(item)

# Code to sort List on date
List_B.sort(key= lambda x:datetime.strptime(x['DOB'], '%d-%m'))

print("\nAfter sorting according to DOB is: ")
for item in List_B:
    print(item)

List_SE_Comp_DOB = []
List_SE_Comp_DOB = List_A + List_B

print("\nResult Merged List sorted according to DOB is: ")
List_SE_Comp_DOB.sort(key= lambda x:datetime.strptime(x['DOB'], '%d-%m'))
for item in List_SE_Comp_DOB:
    print(item)

    
