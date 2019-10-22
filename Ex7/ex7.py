# Print a string
print("Mary had a little lamb.")
# Print a string after calling format
print("Its fleece was white as {}.".format('snow'))
# Print a string
print("And everywhere Mary went.")
# Print a string of 10 '*'
print("." * 10)  # what'd that do?

# set 12 strings
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happens
# Print the string of 12 vars concatenated. 
# If I remove the end = ' ' it prints 2 lines instead of 1
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
