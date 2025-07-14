# pet_module.py

from enum import En

class pet():

    def _init_(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 50
        self.cleanliness = 50

    def feed(self):
        self.hunger = max(0, self.hunger - 20)
        return f"You fed {self.name}. Hunger is now {self.hunger}."
    def bathe(self):
        self.cleanliness = max(0, self.cleanliness - 30)
        return f"You bathed {self.name}. Cleanliness is now {self.cleanliness}."
    def status(self):
        return f"{self.name} the {self.species} \u2794 Hunger: {self.hunger}, Cleanliness: {self.cleanliness}"
    
def welcome_message():
    return "Welcome to the Pet Management System"
