# create a program that will take a user input and print out a list of all the divisors of that number

num = int(input("what number would you like to find the divisors for?:"))

div = []
for x in range(1, num):
    if num % x == 0:
        div.append(x)

print(div)

