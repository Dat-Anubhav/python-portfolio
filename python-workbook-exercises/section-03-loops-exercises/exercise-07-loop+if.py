'''Q7:- Write a program that asks the user to input a number and 
prints all the even numbers from 1 to that number using a for loop.'''

# Taking user input
n=int(input("\nPlease enter the number = "))

print(f"\nEven numbers till {n} are :- ")

for i in range(1,n+1):

    if(i%2==0):

        print(i) # Printing even numbers till n(input number)
