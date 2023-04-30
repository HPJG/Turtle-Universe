import turtle
import math
import time

print('TurtleUniverse! https://github.com/HPJG/Turtle-Universe')


class Orb:

    def __init__(self, x=0, y=0, vx=0, vy=0, radius=0, mass=0):
        self.x, self.y, self.vx, self.vy = x, y, vx, vy
        self.radius, self.mass = radius, mass
        self.star = turtle.Turtle()
        self.star.speed(0)

    def g_update(self, other, prec):
        dis = self.star.distance(other.x, other.y)
        if other.mass > 0 and dis > 0:
            ax = 0
            ay = 0
            h = 0
            a = 0
            ra = 0

            a = other.mass / dis**2
            h = (self.star.towards(other.x, other.y)) % 360

            if 0 <= h < 90:
                ra = math.tan(math.radians(h))
                ax = math.sqrt(a**2 / (ra**2 + 1))
                ay = ra * ax
            elif 90 <= h < 180:
                ra = math.tan(math.radians(h - 90))
                ay = math.sqrt(a**2 / (ra**2 + 1))
                ax = -ra * ay
            elif 180 <= h < 270:
                ra = math.tan(math.radians(h - 180))
                ax = -math.sqrt(a**2 / (ra**2 + 1))
                ay = ra * ax
            elif 270 <= h < 360:
                ra = math.tan(math.radians(h - 270))
                ay = -math.sqrt(a**2 / (ra**2 + 1))
                ax = -ra * ay

            self.vx += ax / prec
            self.vy += ay / prec

    def update(self, prec):
        self.x += self.vx / prec
        self.y += self.vy / prec

        self.star.setheading(
            self.star.towards(self.x + self.vx, self.y + self.vy))
        self.star.goto(self.x, self.y)


class World:

    def __init__(self, skip=2, rate=0, prec=4, size=1, *orbs):
        self.orbs = orbs
        self.rate, self.prec = rate, prec
        self.t = time.time()

        turtle.tracer(skip)
        turtle.setworldcoordinates(-1000 * size, -1000 * size, 1000 * size,
                                   1000 * size)
        turtle.screensize(100000, 100000)

    def update(self):
        for orb in self.orbs:
            for other in self.orbs:
                if orb is not other:
                    orb.g_update(other, self.prec)
            orb.update(self.prec)
        lt = self.t
        self.t = time.time()
        if self.t - lt < self.rate / self.prec:
            time.sleep(self.rate / self.prec + lt - self.t)

    def run(self):
        while True:
            for orb in self.orbs:
                orb.star.penup()
                orb.star.goto(orb.x, orb.y)
                orb.star.pendown()
            self.update()
