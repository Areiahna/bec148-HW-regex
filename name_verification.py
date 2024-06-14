import re

# Problem Statement:  Write a function that takes in a list of names, and verifies that the names are valid names using a regex pattern and match(), and prints the name if it is valid, "Invalid name" if the name is not.

# Expected Outcome:
#------------------
# Abraham Lincoln
# Andrew P Garfield
# Invalid name
# Connor Milliken
# Jordan Alexander Williams
# Invalid name
# Invalid name


names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]

#-- re.match(pattern, text) : will return a match if there is a pattern match at the very beginning of the text

def verify_names(alist):
   for name in alist:
      if re.match(r"[A-Z]+\w+\s+[A-Z]",name):
         print(name)
      else:
         print("Invalid name")
         
verify_names(names)
