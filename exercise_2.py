
# Python Code Challenge: Functions and List Comprehensions
print("-----1111-----")
# Challenge 1: Define a function that takes a list of numbers and returns a new list containing only the even numbers.
# The function should use list comprehension.
numbers=[1,2,3,4,5,6,7,8,9,10]
even_numbers=list(filter(lambda x:x%2 == 0,numbers))
print(even_numbers)

print("--oder---")
numbers=[1,2,3,4,5,6,7,8,9,10]
def even_numbers(number):
  for zahl in numbers:
    if zahl % 2 == 0:
     print(zahl)
#return(zahl)
even_numbers(numbers)

print("-----2222----")
# Challenge 2: Define a function that takes a list of strings and returns a new list with the strings that have more than 5 characters.
# Use list comprehension for filtering.
words=["books", "computers", "laptops", "house","dog"]
new_words= list(filter(lambda s:len(s) > 5,words))
print(new_words)
print("--oder---")
def is_long_string(s):
 return len(s)>5
new_words=list(filter(is_long_string,words))
print(new_words)

print("-----3333----")
# Challenge 3: Write a function that takes a list of integers and returns a list of their squares.
# Use list comprehension to achieve this.
numbers=[1,2,3,4,5,6,7,8,9,10]
squar_numbers=map(lambda x:x**2,numbers)
print(list(squar_numbers))

print("---oder---")

def square(zahlen):
    for x in numbers:
        x = x ** 2
        print(x)
square(list(numbers))
print("-----4444-----")
# Challenge 4: Write a function that accepts two lists of the same length and returns a list of tuples,
# where each tuple contains elements from the two lists at the corresponding positions. Use list comprehension.
words1=["books", "computers", "laptops", "house","dog"]
words2=["chair","desk","tablet","tv"]



"""
def same_length(words):
    for x in words1:
        
    for y in words2:
    #len(x)==len(y)
    print(X,y)
same_length(words1)
same_length(words2)
"""

print("-----555-----")
# Challenge 5: Create a function that takes a sentence (string) and returns a list of the lengths of each word in the sentence.
# Use list comprehension to split the sentence and calculate the lengths.
words1=["books", "computers", "laptops", "house","dog"]
def length(string):
    
    for x in words1:
        y = len(x)

     # print(list(words1,y))
length(words1)
# Challenge 6: Define a function that filters out words from a list that do not start with a vowel.
# Use list comprehension and a helper function that checks if a word starts with a vowel.
words=["books", "computers", "laptops", "house","dog"]
def filter_vowel_words(words):
    vowels='aeiouAEIOU'
    return[word for word in words if word[0]  in vowels]
print(words)
print("-----666-----")
# Challenge 7: Write a function that takes a list of numbers and returns a list of booleans indicating whether each number is greater than 10.
# Use list comprehension for this task.

# Challenge 8: Create a function that takes a list of dictionaries and returns a list of the values for a given key.
# Use list comprehension to extract the values.

# Challenge 9: Write a function that accepts a list of words and returns a list of the words with their first letter capitalized.
# Use list comprehension to achieve this.

print("---999---")

words=["Books", "computers", "Laptops", "house","Dog"]

capitalwords= "A-Z" 
def capital_list(letters):
    if x in words:

     x == capitalwords

     print(X)
capital_list(words)


# Challenge 10: Write a function that returns the common elements between two lists.
# Use list comprehension and the "in" operator to find common elements.

"""
result = common_elements(list1,list2):
 print(result)
"""