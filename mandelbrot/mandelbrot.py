import matplotlib.pyplot as plt
import numpy as np



# https://files.realpython.com/media/latex_mandelbrot.95af84d59784.png
def sequence(c, z = 0):
    while True:
        yield z
        z = z ** 2 + c


def mandelbrot(candidate):
    return sequence(c = candidate, z = 0)

def julia(candidate, parameter):
    return sequence(c = candidate, z = parameter)

def complex_matrix(xmin, xmax, ymin, ymax, pixel_density):
    re = np.linspace(xmin, xmax, int((xmax - xmin) * pixel_density))
    im = np.linspace(ymin, ymax, int((ymax - ymin) * pixel_density))
    return re[np.newaxis, :] + im[:, np.newaxis] * 1j


def is_stable(c, num_iterations):
    z = 0
    for _ in range(num_iterations):
        z = z ** 2 + c
    return abs(z) <= 2

def get_members(c, num_iterations):
    mask = is_stable(c, num_iterations)
    return c[mask]

c = complex_matrix(-2, 0.5, -1.5, 1.5, pixel_density=2100)
members = get_members(c, num_iterations=20)

plt.scatter(members.real, members.imag, color="black", marker=",", s=1)
plt.gca().set_aspect("equal")
plt.axis("off")
plt.tight_layout()
plt.show()






# wrapper()