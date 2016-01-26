# without commas, add new line character is added
# int will convert the string to a integer and use %d

print "How old are you ?" ,
age = int(raw_input())
print "How tall are you ?" ,
height =  raw_input()
print "How much do you weight ?" , 
weight = int(raw_input())

print "So, you're %d years old, %s tall and weigh %d lbs." % (age, height, weight)