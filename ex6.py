# assigns value to the variable
types_of_people = 10
# assigns the variable x, a string value. Remember that f-strings are strings too.
# here the string types_of_people is used inside another string x.
x = f"There are {types_of_people} types of people."

# assigns values to the variables.
binary = "binary"
do_not = "don't"
# here there are strings being used inside another string.
y = f"Those who know {binary} and those who {do_not}."

# prints the inputs
print(x)
print(y)

# prints the f-string. Here both x and y are already strings being places inside another strings.
print(f"I said: {x}")
print(f"I also said: '{y}'")

# assigns values to variables.
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# prints the string joke_evaluation. However the .format function takes the input hilarious and places it in place of {}.
# here too, there is a string being places inside another string.
print(joke_evaluation.format(hilarious))

# assigning strings as values to variables.
w = "This is the left side of..."
e = "a string with a right side."

# python performs the addition operation with two strings as inputs and concatenates the two strings to give an output.
# then it prints it.
print(w + e)
