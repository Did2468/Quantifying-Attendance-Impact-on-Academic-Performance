import matplotlib.pyplot as plt

def scatter_with_line(X, y, model):
    plt.scatter(X, y)
    plt.plot(X, model.predict(X))
    plt.show()
