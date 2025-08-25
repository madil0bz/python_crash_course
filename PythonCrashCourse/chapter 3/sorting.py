# 3-8 Seeing the World: List five places you'd like to visit
locations = ['greenland', 'tokyo', 'switzerland', 'london', 'ibiza']

#print in og order
print(locations)
#print in temporarily sorted order
print(sorted(locations))
#show list is still in original order
print(locations)
#print in temporarily reverse sorted order
print(sorted(locations, reverse=True))
#show list is still in original order
print(locations)

#use reverse to change order of list and show its changed
locations.reverse()
print(locations)
#do it again and show list is back to original order
locations.reverse()
print(locations)

#use sort to change order permenantly and show its changed
locations.sort()
print(locations)

#use reverse sort and show order change
locations.sort(reverse=True)
print(locations)