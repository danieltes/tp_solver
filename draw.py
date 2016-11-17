import matplotlib.pyplot as plt
import compiled


def draw():
    x_points = []
    y_points = []

    for x in range(-1000, 1000):
        try:
            y_points.append(compiled.compiled_func(x))
            x_points.append(x)
        except:
            print("Error, posible discontinuidad en: ", x)
    plt.scatter(x_points, y_points)
    plt.show()
