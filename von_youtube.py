def string(str1):
    count=0
    for char in str1:
        count +=1
    return count
print(string("is python schwer"))


print("----")

#Find length charachter
#1)using for loop 
str="Alles gut"
counter=0
for i in str:
    counter=counter+1
print(counter)

#2)using while loop and slicing

str="everything is good"
counter=0
while str[counter:]:
    counter=counter+1
print(counter)

#3)using built-in function len()
str="ich schaffe das"
print(len(str))

#4)using join and count
str="what do you say"
random_str="X"
print((random_str).join(str))
#show number of x 



