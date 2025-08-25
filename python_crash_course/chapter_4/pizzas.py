#Generate a list of your favourite pizzas
pizzas = ['pepperoni', 'cheese', 'hawaiian']

#use for loop to print name of each pizza
for pizza in pizzas:
    print(f'{pizza}\n')

#print a sentence for each pizza
for pizza in pizzas:
    print(f'{pizza.title()} is a great pizza\n')

#print a statement outside the loop
print(f'I really love pizza!\n')



#copy list of pizzas
friend_foods = pizzas[:]
#add a pizza to the new list
friend_foods.append('canadian')
#print both lists to prove they're different
print(f'My favourite pizzas are:')
for pizza in pizzas:
    print(pizza)

print('\nMy friends favourite pizzas are:')
for pizza in friend_foods:
    print(pizza)