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


this_Tuple = (3,45, "ali", True) # Tuple
this_List = [4,3,"bob", (3,9,"nur")] # this is list
    ## the difference b/w list and tuple is that a tuple cannot change (immutable) while you can change the values of list
    