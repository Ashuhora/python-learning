# This is Escape characters example

text = "The cat said, \"Meow!\"\nThe dog said, \"Woof!\tWoof!\"\n\tThe cow said, \"Moo!\""
print(text)

# This is a  Multi-Line String Art

tree = """                   
   ***
  *****
 *******
   |||
   """

print(tree)

# This is ASCII Art

art = r"""
/\_/\\
(0.o)
 > ^ <

"""
print(art)

# This is Index 

word = input("Please enter any word: ")

print("The first character is:", word[0])
print("The last character is:", word[-1])
print("The length of the word is:", len(word))

# Script : Names

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")

print(first_name.upper() + "\t" + last_name.upper())
print(first_name[0].upper(),last_name[0].upper())
print(last_name.capitalize() + ", " + first_name.capitalize())