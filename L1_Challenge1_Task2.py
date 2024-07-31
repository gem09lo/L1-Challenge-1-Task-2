#L1_Challenge1_Task2.py

"""Task 2a"""
name = (input("What is your name? "))
name = name.title()
#print("Hello {}!".format(name))

"""Task 2b"""
#change name to titlised

if name == "Bob" or name == "Alice":
  print ("Hello {}!".format(name))
else:
  print ("Sorry... You\'re not authorised to be greeted!")
