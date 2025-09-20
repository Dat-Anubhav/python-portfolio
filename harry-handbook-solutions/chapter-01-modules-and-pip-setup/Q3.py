# # install a external module and use it to perform an operation of your interest
# from PyDictionary import PyDictionary
# dictionary = PyDictionary("life"+"sad"+"indentation")
# print (dictionary.synonym("life"))

import pyttsx3
'''engine= pyttsx3.init()
rate=engine.getProperty('rate') # # Function call to getProperty used here.  
# At this stage of learning, I’m exploring functions and will understand them better in upcoming chapters. 
print(rate)
engine.setProperty('rate', 125)
volume=engine.getProperty('volume') # from google 
print(volume) 
engine.setProperty('volume',100)'''

# engine.say("hello how are you")
# engine.say("have a great day") # it runs only line 16 rest got ignored

pyttsx3.speak("see you tommorow")
