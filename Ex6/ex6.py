# set the following variable to 10
types_of_people = 10

# Set x to a formatted string with the var interpolated
x = f"There are {types_of_people} types of people."

# Set var to text
binary = "binary"

# Set the var to text
do_not = "don't"

# Set y to a string with 2 interpolated vars
y = f"Those who know {binary} and those who {do_not}."

# print x
print(x)
# print y
print(y)

# Print text and value of x
print(f"I said: {x}")
# Print text and value of y
print(f"I also said: '{y}'")

# set value to boolean value
hilarious = False
# Set var to string with a placeholder for format
joke_evaluation = "Isn't that joke so funny?! {}"

# print string after formatting and supplying argument for placeholder
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
