"""Define useful math functions and constants."""

pi = 3.1415926535897932384626433832795028841971  # Value of constant pi


def factorial(n):
    """Return the factorial of n."""
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def deg(x):
    """Convert degrees to radians."""
    rad = x * pi/180
    return rad


def sin(x):
    """Approximate sinus(x) for any x (radians) using Taylor expansion."""
    x = x % (2 * pi)
    if x > pi:
        x -= 2 * pi
    sinx = 0
    for k in range(15):
        sinx += (-1)**k * x**(2*k + 1) / factorial(2*k + 1)
    return sinx


def cos(x):
    """Approximate cosinus(x) for any x (radians) using Taylor expansion."""
    x = x % (2 * pi)
    if x > pi:
        x -= 2 * pi
    cosx = 0
    for k in range(15):
        cosx += (-1)**k * x**(2*k) / factorial(2*k)
    return cosx
