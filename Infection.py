#!/usr/bin/env python3

import pygame 
from settings import Settings 
from crowd import Crowd 
import matplotlib.pyplot as plt


# Simulation performed in pygame 
def run_simulation():

    pygame.init()
    clock = pygame.time.Clock()
    settings = Settings()
    sreen_size = (settings.screen_width, settings.screen_height)
    screen = pygame.display.set_mode(sreen_size)
    
    # Crowd object 
    crowd = Crowd(1/settings.N)

    # Data arrays 
    time = [] 
    S_vec, I_vec, R_vec = [], [], []

    # Run 
    running = True
    while running:  
        
        clock.tick(settings.fps)
        screen.fill(settings.screen_color)

        # Crowd object methods 
        crowd.draw(screen)
        crowd.move()
        crowd.infection_spread()
        crowd.recover()

        # Collect data
        [S, I, R] = crowd.get_stats()

        time.append(pygame.time.get_ticks()/1000)
        S_vec.append(S)
        I_vec.append(I)
        R_vec.append(R)

        # When all infected people have recovered
        if I == 0:
             return time, S_vec, I_vec, R_vec 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False     

        pygame.display.flip()
    pygame.quit()
    
    return [time, S_vec, I_vec, R_vec]


# Plotting of results
def plot_results(t, S, I, R):
    fig = plt.figure(figsize = (8, 6))
    plt.xlabel('Time')
    plt.ylabel('People')
    plt.plot(t, S, color = 'blue', label = 'Susceptible')
    plt.plot(t, I, color = 'red', label = 'Infected')
    plt.plot(t, R, color = 'green', label = 'Recovered')
    plt.legend(loc = 'upper right')
    plt.title('Infectious Disease Spread with Increasing Time')
    plt.grid()
    plt.show()



if __name__ == '__main__':
    [t, S, I, R] = run_simulation()
    plot_results(t, S, I, R)