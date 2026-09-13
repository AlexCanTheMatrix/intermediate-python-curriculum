# Problem 1
# Ask the user for their name and age.
# Print a sentence that uses both variables.
nameandage=input("What is your name and how old are you: ")
vars = nameandage.split(" ")
print("Your name is ",vars[0])
print("And your age is",vars[1])

# Problem 2
# Ask the user for a number.
# Print "Positive" if it is more than 0.
# Print "Zero" if it is equal to 0.
# Otherwise print "Negative".
num = int(input("Pick any number"))
if num > 0:
    print("positive")
elif num ==0:
    print("zero")
else:
    print("negative")

# Problem 3
# Create a list of 5 numbers.
# Print the sum of all numbers in the list.
numbers= [5,3,7,1,9]
thesum = 0
for num in numbers:
    thesum=thesum+num

print("The sum is ", thesum)


# Problem 4
# Create a list of 5 animals.
# Count how many times "cat" appears in the list.
animals=["dog", "cat", "aligator", "cat", "hamster"]
count = 0
for animal in animals:
    if animal == "cat":
        count = count +1
print("There are", count,"cats in the list")

# Problem 5
#Ask the user for 2 numbers
# Create a function called bigger(a, b).
# It should return the bigger number.
# Call it and print the result.
def bigger(a,b):
    if a > b:
        return a
    else:
        return b

print(bigger(2,5))
