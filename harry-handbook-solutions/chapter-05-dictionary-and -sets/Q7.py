# Q7:- If the names of 2 friends are same; what will happen to the program in problem
# 6?

'''Q6:-Create an empty dictionary. Allow 4 friends to enter their favorite language as
value and use key as their names. Assume that the names are unique

l1=input("mr anubhav enter your favourite language as value for dictionary :-  ")
l2=input("mr krishna enter your favourite language as value for dictionary :-  ")
l3=input("miss radha enter your favourite language as value for dictionary :-  ")
l4=input("miss bhavani enter your favourite language as value for dictionary :-  ")

dic={}# dictionary is in curly bracket list is in braces this is an empty dictionary

dic.update({"anubhav":l1})
dic.update({"krishna":l2})
dic.update({"radha":l3})
dic.update({"bhavani":l4})
print(dic)'''


l1=input("mr anubhav enter your favourite language as value for dictionary :-  ")
l2=input("mr krishna enter your favourite language as value for dictionary :-  ")
l3=input("miss radha enter your favourite language as value for dictionary :-  ")
l4=input("mr krishna enter your favourite language as value for dictionary :-  ")

dic={}# dictionary is in curly bracket list is in braces this is an empty dictionary

dic.update({"anubhav":l1})
dic.update({"krishna":l2})
dic.update({"radha":l3})
dic.update({"krishna":l4})
print(dic)

# will choose only one i.e the last krishna from the both the keys because dictionary keys are unique and immutable
#  whole dictionary is mutable means we can make changes in the original dictionary
#  but keys are unique and immutable
#  but value can be same for two different keys like in real dictionary