'''Q4 :- What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?'''

s=set()# created an empty set
s.add(20)#integer value
s.add(20.0)#float value
s.add('20')# string value
print(len(s))