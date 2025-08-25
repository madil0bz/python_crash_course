#store five foods in a tuple
menu = ('mac and cheese', 'chicken fingers', 'salad', 'burger', 'potato skins')

#print each food
print(f'original menu:')
for food in menu:
    print(food)

print('\n')
#change the menu
menu = ('mac and cheese', 'cannoli', 'salad', 'burger', 'pie')
print('new menu:')
for food in menu:
    print(food)
