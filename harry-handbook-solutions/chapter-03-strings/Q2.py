"""Q2 :- Write a program to fill in a letter template given below with name and date.
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
''' """
# name = input("enter your name :- ")
# date = input("enter the date :- ")
# print(f"Dear {name} \n you are selected! \n {date} CONGRATULATIONS")

Name = "Anubhav"
Date = "14 september"
letter = "Dear <name>,\nYou are selected!\n<date>\nCONGRATULATIONS" 
M= letter.replace("<name>",Name).replace("<date>",Date)

print(M)