

G = 6.67430*10**-11

class Planets:

    class DistanceFromTheSun:   #In Meters
        saturn = 1492400028000
        jupiter = 778330257000
        uranus = 2870989228000
        neptune = 4504299579000
        mercury = 57910006000
        mars = 227939920000
        venus = 108199995000
        earth = 149597870700

    class Radius:   #In Meters
        saturn = 58.232*10**6
        jupiter = 69.911*10**6
        uranus = 25.362*10**6
        neptune = 24.622*10**6
        mercury = 2.4397*10**6
        mars = 3.3895*10**6
        venus = 6.0518*10**6
        sun = 696.340*10**6
        earth = 6.371*10**6

    class MassOfPlanet:   #In Kilograms
        saturn = 5.6846*10**26
        jupiter = 1.8986*10**27
        uranus = 8.6813*10**25
        neptune = 1.0243*10**26
        mercury = 3.33022*10**23
        mars = 6.4171*10**23
        venus = 4.8675*10**24
        sun = 1.98892*10**30
        earth = 5.9736*10**24


def The_force_acting_on_a_body(m1, m2, r):
    F = G * ((m1 * m2) / r**2)
    return F


def The_gravity_of_a_object(m1, r):
    print(G)
    g = G * (m1 / r**2)
    return g

def Centripetal_Force(m1, r, v):
    return (m1 * v**2) / r

print(str(The_force_acting_on_a_body(Planets.MassOfPlanet.earth, 35786000, 2000)) + " N/m")
print(str(The_gravity_of_a_object(Planets.MassOfPlanet.earth, Planets.Radius.earth)) + " m/s²")
print(str(Centripetal_Force(100, 200000, 20)) + " N/m")


    