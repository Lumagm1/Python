# Write code below 💖

class Pokemon:
    def __init__(self,entry,name,types,description,is_caught):
        self.entry = entry
        self.name = name
        self.types = types
        self.description = description
        self.is_caught = is_caught
    def speak(self):
        print(self.name)
        print(self.name)
    def display_details(self):
        print(f'Entry Number: {self.entry}')
        print(f'Name: {self.name}')
        print(f'Type: {self.types}')
        print(f'Description: {self.description}')
        if(self.is_caught == True):
            print(f'{self.name} has already been caught!')
        else:
            print((f'{self.name} has not been caught!'))
        
pikachu = Pokemon(12,'Pikachu','Electric','Sooo Adorable', True)
dragonite = Pokemon(54, "Dragonite",'Dragon', "Flys with a cute nose", False)
snorlax = Pokemon(17, 'Snorlax','Normal','Snorlax sleeps', True)

pikachu.speak()
pikachu.display_details()
dragonite.speak()
dragonite.display_details()
snorlax.speak()
snorlax.display_details

