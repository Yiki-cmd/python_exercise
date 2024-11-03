# 1. Define two variables, x and y, with values 5 and 10.
#    Perform the following operations and print the results:
#    a) Sum of x and y
#    b) Difference of y and x
#    c) Product of x and y
#    d) Quotient of y by x

x = 5
y = 10
'Answer'
#a)
sum=x+y
print(sum)
#b)
Difference=y-x
print(Difference)
#c)
Product=x*y 
print(Product)
#d)
Quotient= y/x
print(Quotient)
# 2. Define a list of fruits containing "apple", "banana", and "cherry".
#    a) Add "orange" to the list.
#    b) Remove "banana" from the list.
#    c) Print the first and last elements of the list.

fruits = ["apple", "banana", "cherry"]
'Answer'
#a)
fruits.append("orange")
print(fruits)
#b)
fruits.remove("banana")
print(fruits)
#c)
print(fruits[0])
print(fruits[2])

print("--------------------111111111111111----------------------")
# 3. Define a set of numbers containing 1, 2, 3, 4, and 5.
#    a) Add the number 6 to the set.
#    b) Remove the number 3 from the set.
#    c) Check if the numbers 5 and 7 are in the set, and print the results.

numbers_set = {1, 2, 3, 4, 5}
'Answer'
#a)
numbers_set=list(numbers_set)
numbers_set.append(6)
print(numbers_set)
#b)
numbers_set.pop(3)
print(numbers_set)
#c)
i=0
if numbers_set[i]==5 or 7:
 i+=1
print(numbers_set)


# 4. Define a tuple representing coordinates (10.5, 20.7).
#    a) Print the x (first) and y (second) coordinates separately.

coordinates = (10.5, 20.7)
x, y = coordinates
print(x)
print(y)
# 5. Define a dictionary of student grades, where:
#    - "Alice" has a grade of 85
#    - "Bob" has a grade of 90
#    - "Charlie" has a grade of 78
#    a) Add a new student "David" with a grade of 88.
#    b) Update Alice's grade to 95.
#    c) Print Bob's grade.

grades = {"Alice": 85, "Bob": 90, "Charlie": 78}

#'Answer'
#a)
grades["David"] = 78
grades["Alice"] = 95

print(grades["Bob"])

#C)

score=90
if score>=90:
 print("A")
elif score>=80:
 print("B")
elif score>=70:
 print("C")
else:
 print("fail")

print("------------222222222222222222222222222----------------")

# 6. Define a variable called `age` with a value of 18.
#    a) Write an if/else statement that checks if the age is 18 or above. 
#    If true, print "You are eligible to vote", otherwise print "You are not eligible to vote".
"Answer"
age = 18
if age>=18:
 print("above 18")
else:
 print("below 18")


# 7. Define a list of fruits: ["apple", "orange", "grape"].
#    a) Use a `for` loop to print each fruit in the list.

fruits = ["apple", "orange", "grape"]

for i in range(0,3,1):
 print(fruits[i])


# 8. Define a variable `count` with a value of 5.
#    a) Use a `while` loop to print a countdown from 5 to 1.

#a)
count = 5
while count<=1:
  print(count)
  count-=1




# 9. Challenge: Combine lists, sets, dictionaries, and loops.
#    a) Define a list of numbers from 1 to 10.
#    b) Create a set of even numbers from the list using a `for` loop or comprehension.
#    c) Create a dictionary that maps each even number to its square.
#    d) Print the set of even numbers and the dictionary.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#"Answer"
#a)
i=1
if i<=10:
 print(numbers[i])
i+=1


#b)
for i in range(0,11,2):
    print(i)

 
#c)
keys=numbers
values=numbers
print(keys,values)

#d)




print("----------------------------3333333333333333-------------")


# 10. Conversion between List, Set, and Tuple
#     a) Convert the list of fruits to a set and print the result.
#     b) Convert the set of even numbers to a tuple and print the result.
#     c) Convert the tuple of coordinates to a list and print the result.

# Conversion between list, set, and tuple examples:
# fruits -> set
# even_numbers (from challenge) -> tuple
# coordinates (tuple) -> list

#"Answer"
#a)
fruits={"apple", "banana", "cherry"}
fruits=list(fruits)
print(fruits)
fruits=set(fruits)
print(fruits)
fruits=tuple(fruits)
print(fruits)

#b)
"""
for i in range(0,11,2):
print(tuple.(i))
 
"""

# 11. Dictionary Keys and Values
#     a) Print the list of dictionary keys from the `grades` dictionary.
#     b) Print the list of dictionary values from the `grades` dictionary.
#     c) Loop through the dictionary and print each student name (key) and their grade (value).

# Dictionary keys and values
# grades -> keys() -> list
# grades -> values() -> list
# loop through dictionary

#"Answer"

#a)
grades={"Alice": 85, "Bob": 90, "Charlie": 78}
keys = list(grades.keys())

print("name:",keys)



#b)
print(grades.values())

#c)
