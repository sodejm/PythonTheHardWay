#Exercise 6

x = "There are %d types of people." % 10 #set x
binary = "binary"
do_not = "don't" #contraction example
y = "Those who know %s and those who %s." % (binary, do_not) #set y

print x
print y

print "I said: %r." % x #%s will work fine too
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e #concatonation
#same as "This is" + "a Concatonated String"
