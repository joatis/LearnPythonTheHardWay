# Initialize a string called formatter
formatter = "{} {} {} {}"

# call the format function on formatter passing 4 integers
print(formatter.format(1, 2, 3, 4))
# call the format function on formatter passing 4 strings
print(formatter.format("one", "two", "three", "four"))
# call the format function on formatter passing 4 booleans
print(formatter.format(True, False, False, True))
# call the format function on formatter passing 4 instances of the formatter string
print(formatter.format(formatter, formatter, formatter, formatter))
# call the format function on formatter passing 4 strings
print(formatter.format(
  "Try your",
  "Own text here",
  "Maybe a poem",
  "Or a song about fear"
))
