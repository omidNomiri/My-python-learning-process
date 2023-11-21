import math

def solve_cubic(a, b, c, d):
    a, b, c = b/a, c/a, d/a

    q = (3*c - (b**2))/9
    r = (9*b*c - 27*d - 2*(b**3))/54
    d = q**3 + r**2

    if d >= 0:
        s = math.cbrt(r + math.sqrt(d))
        t = math.cbrt(r - math.sqrt(d))

        x1 = -b/3 + (s + t)
        x2 = -b/3 - (s + t)/2 + math.sqrt(3)*(s - t)*1j/2
        x3 = -b/3 - (s + t)/2 - math.sqrt(3)*(s - t)*1j/2

    else:
        th = math.acos(r/math.sqrt(-(q**3)))
        x1 = 2*math.sqrt(-q)*math.cos(th/3) - b/3
        x2 = 2*math.sqrt(-q)*math.cos((th + 2*math.pi)/3) - b/3
        x3 = 2*math.sqrt(-q)*math.cos((th + 4*math.pi)/3) - b/3

    return (x1, x2, x3)

a = 1
b = -6
c = 11
d = -6

roots = solve_cubic(a, b, c, d)

print("roots: ", roots)
