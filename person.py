import pygame 
import random 
import numpy as np 
from settings import Settings 


settings = Settings()

# Person class
class Person:
    
    # Input: S, I, or R 
    def __init__(self, state):
        self.states = {'Susceptible': (0, 0, 230),   #Blue
                    'Infected': (230, 0, 0),    #Red
                    'Recovered': (0, 150,0)     #Green
                    }
        # Random position and momentum 
        self.x = random.randint(0, settings.screen_width)
        self.y = random.randint(0, settings.screen_height)
        self.vel_x, self.vel_y =  random.randrange(-1, 2, 2)*round(random.random(), 5),  random.randrange(-1, 2, 2)*round(random.random(), 5)
        mag = np.sqrt(self.vel_x*self.vel_x + self.vel_y*self.vel_y)

        # Normalized velocity
        self.vel_x, self.vel_y = 2*self.vel_x/mag, 2*self.vel_y/mag

        # Ball settings
        self.state = state 
        self.color = self.states[self.state]
        self.radius = settings.radius 
        
        # Probability of infection 
        self.prob_of_infection = settings.prob_of_infection

        self.clock = pygame.time.Clock()
        self.infection_time = 0
        self.infection_range = (settings.infection_range)*(settings.infection_range)    
        
    # Draw person object to screen
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    # Move person object 
    def update(self):
        if self.x < 0 or self.x > settings.screen_width:
            self.vel_x = -self.vel_x
            self.x += self.vel_x
            self.y += self.vel_y
        elif self.y < 0 or self.y > settings.screen_height:
            self.vel_y = -self.vel_y
            self.x += self.vel_x
            self.y += self.vel_y
        else:
            self.x += self.vel_x
            self.y += self.vel_y

    # Access state 
    def get_state(self):
        return self.state

    # Check if person has become infected 
    def check_infection(self, infected_person):
        x_dist = (self.x - infected_person.x)
        y_dist = (self.y - infected_person.y)
        if abs(x_dist) and abs(y_dist) > settings.infection_range/2:
            return False 
        r = round(x_dist*x_dist + y_dist*y_dist - 2*self.radius, 3)
        if r < self.infection_range and self.state == 'Susceptible':
            if self.prob_of_infection > round(random.random(), 3):
                self.state = 'Infected'
                self.color = self.states[self.state]
                return True
            else:
                return False

    # Recovery after infection 
    def recover(self):
        time_now = pygame.time.get_ticks()
        if time_now  - self.infection_time > settings.recovery_time:
            self.state = 'Recovered'
            self.color = self.states[self.state]
            return True
    
