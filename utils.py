import matplotlib.pyplot as plt
import numpy as np


def gen_data():
    x = np.linspace(-5, 5, num=100)
    y = 0.5 * x + np.random.normal(0, 0.5, 100)
    return x, y


def scatter(x, y):
    plt.title("scatter")
    plt.scatter(x, y, color="red")
    plt.show()


def plot_line(model, x, y):
    y_pred = model.predict(x)
    plt.plot(x, y_pred)
    plt.scatter(x, y, color="red")
    plt.show()
