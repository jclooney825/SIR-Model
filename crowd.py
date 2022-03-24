import pygame
from person import Person 
from settings import Settings
import math 
from numpy import *

settings = Settings()

# Crowd/Herd class
class Crowd:

    # Input fraction of infected people
    def __init__(self, infected_fraction):
        self.N = settings.N

        infected = int(math.ceil(infected_fraction * self.N))

        # Lists of different groups
        self.susceptible_people = [Person('Susceptible') for i in range(self.N - infected)]
        self.infected_people = [Person('Infected') for i in range(infected)]
        self.recovered_people = []
        
        # Total people 
        self.total_people = self.susceptible_people + self.infected_people + self.recovered_people 

    # Draw all people 
    def draw(self, screen):
        for person in self.total_people:
            person.draw(screen)

    # Move all people 
    def move(self):
        for person in self.total_people:
            person.update()
    
    # Spread the infection 
    def infection_spread(self):
        for person in self.susceptible_people[:]:
            for i in self.infected_people[:]:
                if person.check_infection(i):
                    self.susceptible_people.remove(person)
                    self.infected_people.append(person)
                    person.infection_time = pygame.time.get_ticks()

    # Recover those infected 
    def recover(self):                                                          
        for person in self.infected_people[:]:
            if person.recover():
                self.infected_people.remove(person)
                self.recovered_people.append(person)

    # Return the number of each group 
    def get_stats(self):
        return len(self.susceptible_people), len(self.infected_people), len(self.recovered_people)