import matplotlib.pyplot as plt
import compiled


def draw():
    x_points = []
    y_points = []

    for x in range(-1000, 1000):
        try:
            y_points.append(compiled.exp(x))
            x_points.append(x)
        except:
            print("Error, posible discontinuidad")
    plt.scatter(x_points, y_points)
    plt.show()
