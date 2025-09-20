# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!
hdic={"khush":"happy",
      "sad":"udaass",
      "gussa":"anger",
      "jalan":"jealousy",
      "kaam":"sex",
      "madhu":"sweet",
      "madira":"wine"}
print(hdic.keys())
l=input("please enter the word to know its translation in english")
print(hdic.get(l))