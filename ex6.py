x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "The who know %s and those who %s." % (binary, do_not) # %s prints strings

print x
print y

print "I said: %r." % x  # %r is used for debugging, print the raw data of a variable
print "I also said: '%s'." % y # print output of y

hilarious = True
joke_evaluation = "Isn't that joke so funny ?! %r"

print joke_evaluation % hilarious  # prints text and value from variable

w = "This is the left of ..."
e =  "a string with a right side."

print w + e  # concatenate 2 strings