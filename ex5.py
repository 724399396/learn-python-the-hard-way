my_name = 'Zed A. Shaw'
my_age = 22 # not a lie
my_height = 170  # meters
my_weight = 46 # kg
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "He's %d meters tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heacy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffe." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
