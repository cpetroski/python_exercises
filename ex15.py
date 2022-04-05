# enables command line arguments
from sys import argv

# notes what our argument is-- there will always be "script"
script, filename = argv

# txt variable opens filename from argv
txt = open(filename)

# prints name of file from argv
print(f"Here's your file {filename}:")
# opens, reads, and prints filename from argv
print(txt.read())

# prints request for input
print("Type the filename again:")
# specifies that variable file_again is what user inputs
file_again = input("> ")

# txt_again variable opens the file named in input
txt_again = open(file_again)

# reads, then prints file from file_again
print(txt_again.read())
txt.close()
txt_again.close()
