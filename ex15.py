#import argv feature from the sys package

from sys import argv

script, filename = argv

txt = open(filename) # open a file

print "Here's your file %r:" % filename
print txt.read() # the read function opens the file from variable txt

print "Type the filename again:"
file_again = raw_input("-> ")

txt_again = open(file_again)

print txt_again.read()
