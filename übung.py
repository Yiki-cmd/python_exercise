"""
print("-----111-----")
number1=[2,4,5,7,3]

def square(numbers):

  for x in number1:
    x = x ** 2
    
print(x)
  #return(number1)
 
square(number1)


"""
x = int(input('enter a number: '))

def even_odd(x):
  if x%2==0:
    print(x, 'is an even number')
  else:
    print(x, 'is an odd number')

even_odd(x)
 

"""
number1=[2,4,5,7,3]
for  number in number1:
 new_numbers=number**2
 print(new_numbers)

list_of_numbers=[1,2,3,4,5,6,7,8,9,10]
print(list_of_numbers[2:10])

def even_numbers(num):
  result=[]
  for x in num:
  #  print(x)
    if x%2 != 0:
      result.append(x)

  print(result)
     
even_numbers(list_of_numbers)

word=["computer", "laptop","mause","telefon",]
def long_words(five):
  result=[]
  for x in five:
    if len(x) > 5:
      result.append(x)
      print(result)

long_words(word)

def square_numbers(zahl):
  result=[]
  for x in zahl:
    x = x**2
    result.append(x)
    print(result)
square_numbers(list_of_numbers)
    


list1=["elephant","cup","charger","numbers"]
list2=["computer", "laptop","mause","telefon"]
def simlar(words):
  result=[]
  for x in words:
 # if len(list1[])=len(list2[])
  result.append(x)
  print(result)
similar(list1,list2)

print("----555----")
list=["computer", "laptop","mause","telefon"]
def length_words(word):
  result=[list]
  x=len(list)
  result1=result.append(x)
  print(result1)
length_words(list)


print("---666----")
words=["computer", "laptop","mause","telefon","apple","ananas"]
def vowel_start(start):
  vowels=tuple("aeiouAEIOU")
  for words in filters:
  if words.startwith(vowels)==True:
      result.append(words)
return(result)
print(result)
vowel_start(words)

 result=[]
 if list startwith aeiouAEIOU
 result1=result.append(list)
 print(result1)
vowel_start(list)




print("---888-----")

words=["computer", "laptop","Mause","Telefon","apple","Ananas"]

def capital_words(alphabet):
  
  if list(words[0]) == A-Z:
print(words)
  
return(alphabet)
capital_words(words)

"""

words=["computer", "laptop","Mause","Telefon","apple","Ananas"]

def strin(characters):
  word for word in words :
  print(word)
strin(words)