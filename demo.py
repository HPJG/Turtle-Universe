import turtleuniverse as tu

w = tu.World(32, 0, 1, 1, tu.Orb(mass=100),
             tu.Orb(x=50, vx=0.5, vy=0.5, mass=0),
             tu.Orb(x=50, vx=1, vy=1, mass=0),
             tu.Orb(x=50, vx=1.2, vy=1.2, mass=0),
             tu.Orb(x=50, vx=1.25, vy=1.25, mass=0),
             tu.Orb(x=50, vx=1.3, vy=1.3, mass=0),
             tu.Orb(x=50, vx=1.4, vy=1.4, mass=0))
w.run()
