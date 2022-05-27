'''
# 1. Write a Python program to get the smallest number from a list.

data=[3,45,22,68,99,5,78,45,1,10]
print(min([3,45,22,68,99,5,78,45,1,10]))
'''
'''
# #2.  Write a Python function to check a list is empty or not.

list=[1,2]
print(len(list))
'''

'''
# #3.  Write a Python program to select an item randomly from a list.

import random

list=[1,2,3,4,5,6,7,8]
print(random.choice(list))
'''

'''
# 4.  Write a Python program to copy a list.

list=[1,2,3,4,"motey",32]
list2=[]
list2=list.copy()
print(list2)
'''

'''
# #5.  Write a Python program to find the 2nd largest number in a list.

list1=[22,64,11,345,23,535,444,64,43]
list2=list(set(list1))
list2.sort()
print("SEcond highest num is:",list2[-2])
'''

'''
# #6.  Write a Python program to print a specified list after removing the 3rd elements.

list=[1,2,3,4,5,6,7,8]
del list[2]
print(list)
'''

'''
# #7. Write a Python program to count the number of even and odd numbers from a series of numbers.

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9) 
count_odd = 0
count_even = 0
for x in numbers:
    if  x % 2==0:
        count_even+=1
    else:
        count_odd+=1
        print("Number of even numbers :",count_even)
        print("Number of odd numbers :",count_odd)
'''
'''
#8. Write a Python program to add an item in a tuple.
original_tuple=(1,2,3,4,5)
print(original_tuple)

original_list=list(original_tuple)

original_list.append("motu")


mixed_tuple=tuple(original_list)

print(mixed_tuple)
'''

'''
#9.  Write a Python program to convert tuple to list.

data_tuple=(1,2,3,4,5)
print(data_tuple)

original_list=list(data_tuple)
print(original_list)
'''

'''
#10.  Write a Python program to convert a tuple to a string.

tuple1=("m","o","t","e","y")

string="".join(tuple1)
print(string)
'''

'''
#11.  Write a Python program to convert a list to a tuple.

list1=[1,2,3,4,5]
print(list1)

tuple1=tuple(list1)
print(tuple1)
'''

'''
#12.  Write a Python Program to Convert List of Tuple into Dictionary

data=[('Key 1', 1), ('Key 2', 2), ('Key 3', 3)]
data1=dict(data)
print(data1)
'''

'''

#13.  Write a Python script to add a key to a dictionary.
#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}

data={0:10,1:20}

add_data={2:30}
data.update(add_data)

print("data after addition of key",data)
'''
'''
#14. Write a Python script to concatenate following dictionaries to create a new one.
#Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
new_dict=dic1.copy()
new_dict.update(dic2|dic3)
print("dictionary after concatination",new_dict)
'''

'''
#15.  Write a Python script to check if a given key already exists in a dictionary.

data={"name":"motu",'age':22}
get_data=data.get('name')

print(get_data)
'''

'''
#16.  Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
#Sample Dictionary{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}


d=dict()
for x in range(1,16):
    d[x]=x**2
print(d)
'''
'''
#17. Write a Python script to merge two Python dictionaries.

dict1={"name":"moyu","age":20}
dict2={"address":"ktm","weight":60}

dict1.update(dict2)
print(dict1)
'''

'''
#18. Write a Python program to find the 3nd largest number in a list.
list1=[22,64,11,345,23,535,444,64,43]

list2=list(set(list1))
list2.sort()

print("Third largest num is ",list2[-3])
'''
'''
##19. Write a Python program to create a set.

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
new_set=A|B
print(new_set)

'''

