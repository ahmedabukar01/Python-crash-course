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
test_list = [1,2,3,4,5]
atest = {"a":"ahmed", "b": "nur", "date": 39}

for k in atest.keys():
    print(k)
    for v in atest.values():
        print(v)
        for i in atest.items():
            print(i)
            for k,v in atest.items():
                print(k,v)
    