# Q2:- Write a program to accept marks of 6 students and display them in a sorted
# manner.
s1=int(input("enter the marks of the first student :-"))
s2=int(input("enter the marks of the second student :-"))
s3=int(input("enter the marks of the third student :-"))
s4=int(input("enter the marks of the fourth student :-"))
s5=int(input("enter the marks of the fifth student :-"))
s6=int(input("enter the marks of the sixth student :-"))
# s7=input("enter the marks of the seventh student :-")
# note:- if you dont take the input in int then it will sorted 
# according to ASCII code hence 123 can come before 45 use input 
# in int or specify it in sorted method as sorted(stlist, key=int)
stlist=[s1,s2,s3,s4,s5,s6]
print("student list is :- ",stlist)
m=sorted(stlist)
print("the sorted list is :- ",m)

# do this tommorow
""" stlist = ['12', '23', '123', '45', '67', '78']
m = sorted(stlist, key=int) # Convert to int for sorting
print("the numerically sorted list is :- ", m)"""
