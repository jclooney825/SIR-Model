import pygame 

# Simulation Settings
class Settings:

    def __init__(self):

        # Screen Settings
        self.screen_width = 1000
        self.screen_height = 700
        self.screen_color = (150,150,150)

        # FPS
        self.fps = 60 

        # Number of people 
        self.N = 250

        # Ball radius 
        self.radius = 3
        
        # Simulation settings 
        self.infection_range = 10 
        self.recovery_time = 5000 # ms 
        self.prob_of_infection = 0.75