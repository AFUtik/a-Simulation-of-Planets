

import TSOTSS as ts


sun = ts.Planet(0, 0, 30, ts.YELLOW, 1.98892*10**30)
sun.sun = True

earth = ts.Planet(-1 * ts.Planet.AU, 0 , 16, ts.BLUE,  5.9736*10**24)
earth.y_vel = 29.783 * 1000

mars = ts.Planet(-1.524 * ts.Planet.AU, 0, 12, ts.RED, 6.39 * 10**23)
mars.y_vel = 24.077 * 1000

mercury = ts.Planet(0.387 * ts.Planet.AU, 0, 8, ts.DARK_GREY, 3.30 * 10**23)
mercury.y_vel = -47.4 * 1000

venus = ts.Planet(0.723 * ts.Planet.AU, 0, 14, ts.WHITE, 4.8685 * 10**24)
venus.y_vel = -35.02 * 1000

jupyter = ts.Planet(-5.2 * ts.Planet.AU, 0, 20, ts.BROWN, 1.8986*10**27)
jupyter.y_vel = -13.07 * 1000

saturn = ts.Planet(9.54 * ts.Planet.AU, 0, 12, ts.ORANGE, 58.232*10**6)
saturn.y_vel = -9.690 * 1000

uranus = ts.Planet(19.19 * ts.Planet.AU,0, 16, ts.LIGHT_BLUE,  25.362*10**6)
uranus.y_vel = 6.81 * 1000

neptune = ts.Planet(30.06 * ts.Planet.AU, 0, 14, ts.DEEP_BLUE, 24.622*10**6)
neptune.y_vel = 5.4349 * 1000

planets = [sun, earth, mars, mercury, venus, jupyter, saturn, uranus, neptune]