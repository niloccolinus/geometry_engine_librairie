"""Define useful math functions and constants."""

pi = 3.1415926535897932384626433832795028841971  # Value of constant pi


def factorial(n: int):
    """Return the factorial of n."""
    if n == 1 or n == 0:
        return 1
    elif n < 0:
        raise ValueError("Cannot compute factorial for negative integers.")
    else:
        return n * factorial(n - 1)


def deg_to_rad(x):
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


def tan(x):
    """Approximate tangent(x) for any x (radians) using sin and cos."""
    if abs(cos(x)) < 1e-9:
        raise ValueError("Tangent is undefined for this angle (cosine is zero).")  # noqa: E501
    return sin(x) / cos(x)


def is_close(a, b, rel_tol=1e-9, abs_tol=0.0):
    """Determine whether two floating-point numbers are approximately equal."""
    return abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)


def abs(x):
    if (x < 0):
        return -x
    else:
        return x


def root(x, n=2):
    """Returns nth root of x with a parameter n defined at 2 by default"""
    return x ** (1/n)
