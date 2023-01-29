# a-Simulation-of-Planets
In order to run this project you need module Pygame how to install this module is written below

```shell
pip install pygame
```

Next, What you can do in the project you can
create planets and watch how planets behave with gravitation
so, you need to know hotkeys:
               
* Z - Decreases time speed           
* X - Increases time speed
* O - Turn on the orbit and turn off the orbit                                   
* LMB - create a planet
* Mouse wheel - zoom

If you want change limit of allowed lines just change the variable
```py
your_limit = 300
```
or you want to add a planet to the solar system find class Planets and create Planet after that add the variable to the list   

Example:
```
planet = Planet(x, y, radius, color, mass)
```                           
if you pass value only on axis x: `planet.y_vel = your_speed` or if you pass value only on axis y: `planet.x_vel = your_speed` 

```py
neptune = Planet(30.06 * Planet.AU, 0, 14, DEEP_BLUE, 24.622 ** 10 * 6)
neptune.y_vel = 5.4349 * 1000
```
then add the varible to the list
```py
planets = [sun, earth, mars, mercury, venus, jupyter, saturn, uranus, neptune]
```
