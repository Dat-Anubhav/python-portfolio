# Q2:-Write a program to input eight numbers from the user and display all the unique
# numbers (once)
l1=int(input("eneter the number :- "))
l2=int(input("eneter the number :- "))
l3=int(input("eneter the number :- "))
l4=int(input("eneter the number :- "))
l5=int(input("eneter the number :- "))# here is the input of all the 8 numbers from the user
l6=int(input("eneter the number :- "))
l7=int(input("eneter the number :- "))
l8=int(input("eneter the number :- "))
s=set()#made an empty set in which i will store all the other inputs from the user
s.add(l1)# a set can input only one at a timel1,l2,l3 not valid
s.add(l2)
s.add(l3)
s.add(l4)
s.add(l5)
s.add(l6)
s.add(l7)
s.add(l8)

print("all the unique numbers are :- ",s)