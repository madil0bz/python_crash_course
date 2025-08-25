#Print the numbers 1-20
for value in range(1, 21):
    print(value)

#make a list from one to one million and print the min, max, and sum
numbers = list(range(1, 1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

#print odd numbers from 1-20 using range
for value in range(1, 21, 2):
    print(value)

#make a list of multiples of three and print
numbers_2 = list(range(3, 33, 3))
for number in numbers_2:
    print(number)

#Make a list of 1-10 cubed and print
numbers_cubed = []
for value in range(1, 11):
    cube = value **3
    numbers_cubed.append(cube)

for value in numbers_cubed:
    print(value)

#use list comprehension to generate a list of the first 10 cubed
cubes = [value**3 for value in range(1, 11)]
print(cubes)