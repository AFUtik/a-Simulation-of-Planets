
import planets as pls
import pygame
import math
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



FONT = pygame.font.SysFont("comicsans", 16)

time_speed = 1

win_text = FONT.render((1 * time_speed) + "x")
pos = win_text.get_rect(20, 10)

#theta = math.atan2(distance_y, distance_x)#



class Planet:

    G = 6.67428e-11

    AU = 149.6e6 * 1000
    
    LY = 9.461e+12 #Light Year

    TIMESTEP = 3600*24

    SCALE = 150 / AU

    Decrease = 1

    direction_y = 0

    direction_x = 0

    Lines = True


    def __init__(self, x, y, radius, color, mass):
        self.color = color
        self.radius = radius
        self.mass = mass
        self.x = x
        self.y = y
        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0



    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2

        if len(self.orbit) > 2 and Planet.Lines == True: 
            updated_points = []
            
            for point in self.orbit:
                x, y = point
                x = x * self.SCALE + WIDTH / 2
                y = y * self.SCALE + HEIGHT / 2
                updated_points.append((x, y))


            pygame.draw.lines(win, self.color, False, updated_points, 2)

        pygame.draw.circle(win, self.color, (x, y), self.radius * Planet.Decrease)



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



    def update_position(self, planets):
        total_fx = total_fy = 0
        for planet in planets:
            if self == planet:
                continue

            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.x_vel += total_fx / self.mass * self.TIMESTEP
        self.y_vel += total_fy / self.mass * self.TIMESTEP

        self.x += self.x_vel * self.TIMESTEP
        self.y += self.y_vel * self.TIMESTEP
        self.orbit.append((self.x, self.y))


def main():
    run = True
    clock = pygame.time.Clock()


    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))

        for event in pygame.event.get():

            #TIME
            increases_speed_of_time = pygame.key.get_pressed()

            decreases_speed_of_time = pygame.key.get_pressed()
            if increases_speed_of_time[pygame.K_x]:
                Planet.TIMESTEP *= 2
            if decreases_speed_of_time[pygame.K_z]:
                Planet.TIMESTEP /= 2


            #ORBITAL
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o and Planet.Lines is True:
                    Planet.Lines = False
                    
                elif event.key == pygame.K_o and Planet.Lines is False:
                    Planet.Lines = True  
                    
            #ZOOM
            if event.type == pygame.MOUSEWHEEL:
                if event.y == 1:
                    Planet.Decrease *= 2
                    Planet.SCALE *= 2
                else:
                    Planet.Decrease /= 2
                    Planet.SCALE /= 2
            if event.type == pygame.QUIT:
                run = False

        
        

        for planet in pls.planets:
            planet.update_position(pls.planets)
            planet.draw(WIN)

        


        pygame.display.update()

    pygame.quit()
    
main()





