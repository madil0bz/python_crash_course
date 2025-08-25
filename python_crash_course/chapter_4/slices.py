#print first three, middle three, and last three items of a list
numbers = list(range(1,10))
#first three
for value in numbers[:3]:
    print(value)

#middle three
for value in numbers[3:-3]:
    print(value)

#last three
for value in numbers[-3:]:
    print(value)