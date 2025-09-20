'''Q6:-Create an empty dictionary. Allow 4 friends to enter their favorite language as
value and use key as their names. Assume that the names are unique'''

l1=input("mr anubhav enter your favourite language as value for dictionary :-  ")
l2=input("mr krishna enter your favourite language as value for dictionary :-  ")
l3=input("miss radha enter your favourite language as value for dictionary :-  ")
l4=input("miss bhavani enter your favourite language as value for dictionary :-  ")

dic={}# dictionary is in curly bracket list is in braces this is an empty dictionary

dic.update({"anubhav":l1})
dic.update({"krishna":l2})
dic.update({"radha":l3})
dic.update({"bhavani":l4})
print(dic)