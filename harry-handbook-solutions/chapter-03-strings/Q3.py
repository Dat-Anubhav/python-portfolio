# Q3 :- Write a program to detect double space in a string.
# str = input("enter the string :- ")
''' whenever a user input 
it gets stored in a string data type even if you input a space it also count as a string character 
thats why strip function is not working'''
str = "     Anubhav    srivastav    "
m = str.strip( )
if(m!=str): # you can just use str.find("  ") if it gives minus -1 then no double space
    #  if any other index nubmber means it has double space at that index number 
    print("there is double or extra space in the string and the modified string is :-",m)
else:
    print("there is no extra or double space in the string")


#Q4:- Replace the double space from problem 3 with single spaces.

m=str.replace("  "," ")
print(m)