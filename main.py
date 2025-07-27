import math


# user_input = input("please input name")

# print(f"welcome {user_input} to the club!")

# pythagorean theorem 
a_side = int(input("please input a side of the triangle: "))
b_side = int(input("please input b side of the triangle: "))

    # the formal is square_root(a^2 + b^2)
pythagorean = math.sqrt(a_side**2 + b_side**2)

print(f"the c type of triangle is: {pythagorean}")
# print(f"the c type of triangle is: ", round(pythagorean, 2)) # minimize decimal points


# Containers
a_Tuple = (3,45, "ali", True) # Tuple
a_List = [4,3,"bob", (3,9, 9, "nur")] # list.
    ## the difference b/w list and tuple is that a tuple cannot change (immutable) while you can change the values of list
a_List.append("another name")

a_set = {3,4,"ahmed"} # set, every entry is unique .
print(set(a_List)) # you can get the list with unique values only, no doublicates
a_dictionary = {"name": "bob", "age": 34} # key value pair.

