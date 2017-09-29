# Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# 40320



from datetime import datetime

user_input = int(input("Please enter number: "))

print ("\nWhile loop:")
startTime = datetime.now()

answer = user_input
i = user_input

while i !=1:
    answer *= (i-1)
    i -= 1

print ("n! of", user_input, "is", answer)

print ("\nScript running time: ", datetime.now() - startTime, "\n")

print ("\nfunction:")
startTime = datetime.now()

def fact(x):
    if x==0:
        return 1
    return x * fact(x-1)

print ("n! of", user_input, "is", fact(user_input))
print ("\nScript running time: ", datetime.now() - startTime, "\n")
