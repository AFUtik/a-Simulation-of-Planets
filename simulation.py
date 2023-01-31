import pygame
import math
import random
from typing import Tuple

pygame.init()

WIDTH, HEIGHT =  1980, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)
RED = (188, 39, 50)
DARK_GREY = (80, 78, 81)
BROWN = (106, 60, 31)
ORANGE = (218, 79, 0)
LIGHT_BLUE = (62, 142, 182)
DEEP_BLUE = (62, 63, 190)
GRAY = (58, 54, 60)

class Planet:
    G = 6.67428e-11
    AU = 149.6e6 * 1000
    TIMESTEP = 3600*24
    SCALE = 150 / AU
    DECREASE = 1
    LINES = True
    YOUR_LIMIT = 1000
    MOVE = [0, 0]

    def __init__(self, x: float, y: float, radius: int, color: Tuple[int, int, int], mass: float):
        self.color = color
        self.radius = radius
        self.mass = mass
        self.x = x
        self.y = y
        self.orbit = []
        self.sun = False
        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win: pygame.Surface):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2 and Planet.LINES == True: 
            updated_points = []
            for point in self.orbit:
                x, y = point
                x = (x * self.SCALE + WIDTH / 2)
                y = (y * self.SCALE + HEIGHT / 2)

                updated_points.append((x + Planet.MOVE[0] * Planet.DECREASE, y + Planet.MOVE[1] * Planet.DECREASE))  

                if len(updated_points) > Planet.YOUR_LIMIT:
                    del updated_points[0:Planet.YOUR_LIMIT - 2]
                    self.orbit.clear()
                
            if len(updated_points) < Planet.YOUR_LIMIT:
                pygame.draw.lines(win, self.color, False, updated_points, 1)
            
        pygame.draw.circle(win, self.color, (x + Planet.MOVE[0] * Planet.DECREASE, y + Planet.MOVE[1] * Planet.DECREASE), self.radius * Planet.DECREASE)

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        force = self.G * self.mass * other.mass / distance**2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets : tuple):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        if self.mass == 0:
            self.mass = 1

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))

class Planets:
    sun = Planet(0, 0, 30, YELLOW, 1.98892*10**30)
    sun.sun = True
    
    earth = Planet(-1 * Planet.AU, 0 , 16, BLUE,  5.9736*10**24)
    earth.y_vel = 29.783 * 1000
    
    mars = Planet(-1.524 * Planet.AU, 0, 12, RED, 6.39 * 10**23)
    mars.y_vel = 24.077 * 1000
    
    mercury = Planet(0.387 * Planet.AU, 0, 8, DARK_GREY, 3.30 * 10**23)
    mercury.y_vel = -47.4 * 1000
    
    venus = Planet(0.723 * Planet.AU, 0, 14, WHITE, 4.8685 * 10**24)
    venus.y_vel = -35.02 * 1000
    
    jupyter = Planet(-5.2 * Planet.AU, 0, 20, BROWN, 1.8986*10**27)
    jupyter.y_vel = -13.07 * 1000
    
    saturn = Planet(9.54 * Planet.AU, 0, 12, ORANGE, 58.232*10**6)
    saturn.y_vel = -9.690 * 1000
    
    uranus = Planet(19.19 * Planet.AU,0, 16, LIGHT_BLUE,  25.362*10**6)
    uranus.y_vel = 6.81 * 1000
    
    neptune = Planet(30.06 * Planet.AU, 0, 14, DEEP_BLUE, 24.622*10**6)
    neptune.y_vel = 5.4349 * 1000
    
    planets = [sun, earth, mars, mercury, venus, jupyter, saturn, uranus, neptune]

def main():
    start = False
    run = True
    clock = pygame.time.Clock()
    color = (58, 54, 60)
    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))
        for event in pygame.event.get():
            #Movement of camera
            mousewheel = pygame.mouse.get_pressed()
            rel1 = pygame.mouse.get_rel(0, 0)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 2:
                rel1 = (0, 0)
            elif mousewheel[1]:
                Planet.MOVE[0] += rel1[0] / Planet.DECREASE
                Planet.MOVE[1] += rel1[1] / Planet.DECREASE

            #create the planets
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                start = True
                sp = event.pos
            elif event.type == pygame.MOUSEMOTION:
                if start == True:
                    try:
                        pos = event.pos
                    except:
                        pass
                    width = pos[0] - sp[0]

                    #Calculating of mass
                    S = (4 * math.pi) * ((((width / 2 * Planet.AU) ) / 10000000)) ** 2
                    mass = (1880) * S**2

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:

                x = (((WIDTH / 2) - (sp[0] - Planet.MOVE[0] * Planet.DECREASE)) / Planet.SCALE)
                y = (((HEIGHT / 2) - (sp[1] - Planet.MOVE[1] * Planet.DECREASE)) / Planet.SCALE)

                your_planet = Planet(-x, -y, width / 2, color, mass)

                your_planet.x_vel = 23.1 * 1000
                your_planet.y_vel = 3.1 * 1000

                Planets.planets.append(your_planet)

                start = False
            #COLORS
            color_key = pygame.key.get_pressed()
            if color_key[pygame.K_TAB]:
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            #TIME
            speed_of_time = pygame.key.get_pressed()
            if speed_of_time[pygame.K_x] and (Planet.TIMESTEP) < (4 * 3600*24):
                Planet.TIMESTEP *= 2
            elif speed_of_time[pygame.K_z] and (Planet.TIMESTEP) > 0:
                Planet.TIMESTEP /= 2

            #ORBITAL
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o and Planet.LINES is True:
                    Planet.LINES = False                    
                elif event.key == pygame.K_o and Planet.LINES is False:
                    Planet.LINES = True  

            #ZOOM
            if event.type == pygame.MOUSEWHEEL:
                if event.y == 1:
                    Planet.DECREASE *= 2
                    Planet.SCALE *= 2
                else:
                    Planet.DECREASE /= 2
                    Planet.SCALE /= 2
            if event.type == pygame.QUIT:
                run = False

        for planet in Planets.planets:
            planet.update_position(Planets.planets)
            planet.draw(WIN)
        if start == True:
            try:
                pygame.draw.circle(WIN, color, (sp[0], sp[1]),width / 2 * Planet.DECREASE)
            except:
                pass
        pygame.display.update()

    pygame.quit()
    
main()
