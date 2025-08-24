# 3-4 make a guest list and print invitation for their dinner
dinner_guests = ['Bubba', 'Mumma', 'Great Grandma']
print(f'You are invited to dinner {dinner_guests[0]}, {dinner_guests[1]}, and {dinner_guests[2]}!')

#remove and insert a new dinner guest
print(f'unfortunately {dinner_guests[2]} cannot make it!')
del dinner_guests[2]
dinner_guests.insert(2, 'Aunty Sara')
print(f'You are invited to dinner {dinner_guests[0]}, {dinner_guests[1]}, and {dinner_guests[2]}!')

# Add three more guests to invite to dinner
print('Hello guests would just like to inform you we have found a bigger table! This means I will be inviting three additional guests to dinner.')
dinner_guests.insert(0, 'Mitch')
dinner_guests.insert(2, 'Devon')
dinner_guests.append('Hannah')
print(f'You are invited to dinner {dinner_guests[0]}, {dinner_guests[1]}, {dinner_guests[2]}, {dinner_guests[3]}, {dinner_guests[4]}, and {dinner_guests[5]}!')

# now there is only space for two dinner guests
print('Hello valued guests, unfortunately the table wont be arriving on time so we only have space for two guests now :(')
dinner_guests.pop()
dinner_guests.pop()
dinner_guests.pop()
dinner_guests.pop()
print('Mitch and Bubba you are still invited to dinner!')

del dinner_guests[0]
del dinner_guests[0]
#delete everyone and check your list
print(dinner_guests)