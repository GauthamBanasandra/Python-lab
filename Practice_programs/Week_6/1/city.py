class City:	
	def __init__(self, name, places=[]):
		self.name=name
		self.places=places

	def add_place(self, place):
		self.places.append(place) if place not in self.places else print(place, 'is already in the list')
	
	def remove_place(self, place):
		try:
			self.places.remove(place)
		except ValueError as e:
			print(place, 'is not in the list')
		
	def display_places(self):
		print(', '.join(self.places) if len(self.places)!=0 else 'please add some places to visit in '+ self.name)


i=0
c=City(input('enter a city name\n'))
while i!='q':
	print('\t\t\t\t1-add a place to visit in '+c.name)
	print('\t\t\t\t2-remove places from '+c.name)
	print('\t\t\t\t3-display places in '+c.name)
	print('\t\t\t\t4-change city')
	i=input()
	if i=='1':
		c.add_place(input('enter a place to add to the list\n'))
	elif i=='2':
		c.remove_place(input('enter a place to remove from the list\n'))
	elif i=='3':
		c.display_places()
	elif i=='4':
		c=City(input('enter a city name\n'))
		c.places=[]
	else:
		break
