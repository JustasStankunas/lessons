#Question:
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

from datetime import datetime

startTime = datetime.now()
answer = []

for i in range (2000,3201):
    if (i%7==0) and (i%5!=0):
        answer.append(str(i))

print (','.join(answer))

print ("\nScript running time: ", datetime.now() - startTime, "\n")

startTime = datetime.now()
answer = []
i = 2000
while i<=3200:
    if (i%7==0) and (i%5!=0):
        answer.append(str(i))
    i += 1

print(','.join(answer))

print ("\nScript running time: ", datetime.now() - startTime, "\n")
