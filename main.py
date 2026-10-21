import turtle as t, math as m, random as r

SCALE = 100
s = t.Screen(); s.setup(600, 700); s.bgcolor("#050002"); s.tracer(0)
p = t.Turtle(); p.hideturtle(); p.penup()

def heart(u):
    x = 1.6 * (m.sin(u) ** 3)
    y = 1.3 * m.cos(u) - 0.5 * m.cos(2*u) - 0.2 * m.cos(3*u) - 0.1 * m.cos(4*u)
    return x, y

N = 2000
pts = []
for _ in range(N):
    u = r.uniform(0, 2 * m.pi)
    hx, hy = heart(u)
    rad = m.sqrt(r.random())
    x, y = hx * rad, hy * rad
    z = 1.1 * (1 - rad) * r.uniform(-1, 1)
    pts.append((x, y, z))

def get_col(f):
    f = max(0.0, min(1.0, f))
    r1, g1, b1 = 70, 0, 10
    r2, g2, b2 = 255, 30, 50
    return f"#{int(r1+(r2-r1)*f):02x}{int(g1+(g2-g1)*f):02x}{int(b1+(b2-b1)*f):02x}"
