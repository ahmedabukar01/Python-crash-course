# indentation called space tab

import math



# user_input = input("please input name")

# print(f"welcome {user_input} to the club!")

# pythagorean theorem 
# a_side = int(input("please input a side of the triangle: "))
# b_side = int(input("please input b side of the triangle: "))

#     # the formal is square_root(a^2 + b^2)
# pythagorean = math.sqrt(a_side**2 + b_side**2)

# print(f"the c type of triangle is: {pythagorean}")
# # print(f"the c type of triangle is: ", round(pythagorean, 2)) # minimize decimal points


# # Containers
# a_Tuple = (3,45, "ali", True) # Tuple
# a_List = [4,3,"bob", (3,9, 9, "nur")] # list.
#     ## the difference b/w list and tuple is that a tuple cannot change (immutable) while you can change the values of list
# a_List.append("another name")

# a_set = {3,4,"ahmed"} # set, every entry is unique .
# print(set(a_List)) # you can get the list with unique values only, no doublicates
# a_dictionary = {"name": "bob", "age": 34} # key value pair.
# a_dictionary["city"] = "mogadishu" # added new key value.

#     ### slicing
# print(a_List[0:3]) #show from 0 to 3 but not include 3
# print(a_List[0:3:2]) #show from 0 to 3 but take every 2nd element. list[start:stop:step]


# # excercise
# test = (1,2,3,4,5,6,7,8,9,10) # expected outcome 8,6,4,2
# test_sliced = test[7::-2]
# print(test_sliced)


#     # Control Flow
# if 3 > 4: 
#     print("incorrect statement")
# elif 2 > 1: 
#     print("Some other correct")
# else: 
#     print("some thing else")

# counter = 0
# while counter < 10:
#     counter = + 1
#     if counter == 5:
#         print("the counter is equal to 5")
# print(f"the counter is : {counter}")

# for Loop
# test_list = [1,2,3,4,5]
# atest = {"a":"ahmed", "b": "nur", "date": 39}

# for k in atest.keys():
#     print(k)
#     for v in atest.values():
#         print(v)
#         for i in atest.items():
#             print(i)
#             for k,v in atest.items():
#                 print(k,v)

### Functions
# def testing_function(text="Hello World!", stop=4):
#     for i in range(stop):
#         if stop == 10:
#             print("You're Too loud!!!!")
#         else: 
#             print(text)
#         return "done"
    
# print(testing_function("here is the king", 12))

# Single Line if statement
# age = 20
# status = "Adult" if age > 20 else "Child"

# ## list comprehension
# simple_list=[]
# for i in range(0,10,1):
#     simple_list.append(i)
# print(simple_list)

# shortened_simple_list = [i for i in range(0,10,1)]
# print(shortened_simple_list)

# # more complex
# shortened_simple_list = [f'{j}{i}' for i in range(0,10,1) for j in ['a', 'b', 'c']]
# print(shortened_simple_list)

# shortened_simple_list = [f'{j}{i}' for i in range(0,10,1) for j in ['a', 'b', 'c'] if j = 'a']
# print(shortened_simple_list)

# ### Lambda function
# double_value = lambda num: num * 2
# print(double_value(8))

# ### function as argument
# random_list = [1,2,3,1223,9,4,50]
# sorted_list = sorted(random_list)
# print(sorted_list)

# a_random_list = [("anna", 89), ("alex", 55), ("john", 22)]
# a_sorted_list = sorted(a_random_list, key= lambda user_tuple: user_tuple[1]) ## It means: for each user_tuple in the list, use the second element (user_tuple[1], which is the number) as the value to sort by.
# print(a_sorted_list)


# ### exercise
# the_list = [f'{l}{n}' for l in ['a', 'b', 'c', 'd', 'e'] for n in range(1,6,1) if f'{l}{n}' != 'c3']
# print(the_list)


# ### Classes
# class ClassName:
#     var_test = "Hello classes"

#     def test_fun(self): # self is convention, you call call it other names, but it's MUST, function must get argument in class so that they can access attribute inside the class
#         print("function in a class") ## self refers to any instance of the class and must be the first parameter for all methods  

#     def another_func(self, test_param):
#         print(test_param)

# ## class instance
# test = ClassName()
# test.test_fun()
# test.another_func("this is the best")


# variables in class are attributes 
# functions in class are methods


# ### Dunder Methods (special methods in class)  __init__
# class Manga:
#     def __init__(self, health, manga):
#         self.manga = manga
#         self.health = health
#         print('instance was created!')

#     def __repr__(self):
#         return f'a manga with {self.health} hp'

# ### inheritence
# class Fight:
#     def __init__(self, health):
#         self.health = health

#     def attack(self, target):
#         target.health -= 10

# ## inheritance child
# class Monster(Fight):
#     def __init__(self, health):
#         super().__init__(health)

# manga = Manga(100, 100)
# monster = Monster(100)
# monster.attack(manga)
# print(manga)  # this output is from __repr__



### modules / library (e.x: import math)
import random
import string
from string import ascii_lowercase
import support.main
from support.main import MyClass

random_number = random.randint(0,10)
print(random_number)
print(string.ascii_letters)
print(ascii_lowercase)

forignClass = support.main.MyClass()
print(forignClass.a)
forignClass.some_function()