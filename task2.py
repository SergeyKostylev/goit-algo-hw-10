import numpy as np
import scipy.integrate as sci
import matplotlib.pyplot as plt


def f(x):
    return x ** 2

def monte_carlo_integral_calculation(a, b, num_samples=10000):
    x = np.random.uniform(a, b, num_samples)
    y = np.random.uniform(0, f(b), num_samples)
    points_under_curve = np.sum(y <= f(x))
    area_ratio = points_under_curve / num_samples

    total_area = (b - a) * f(b)
    return total_area * area_ratio


if __name__ == "__main__":
    a = 0  # low border
    b = 2  # top border
    numerical_integral, numerical_error = sci.quad(f, a, b)
    print(f"Numerical integral: {numerical_integral} with error {numerical_error}")

    num_samples = [100, 1000, 10000, 100000, 1000000]
    for sample in num_samples:
        mc_result = monte_carlo_integral_calculation(a, b, num_samples=sample)
        print(f"Monte Carlo integral ({sample} points): {mc_result}")

    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    fig, ax = plt.subplots()

    ax.plot(x, y, "r", linewidth=2)

    ix = np.linspace(a, b)
    iy = f(ix)
    ax.fill_between(ix, iy, color="gray", alpha=0.3)

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")

    ax.axvline(x=a, color="gray", linestyle="--")
    ax.axvline(x=b, color="gray", linestyle="--")
    ax.set_title(f"Function graph f(x) = x^2 from {str(a)} to {str(b)}")
    plt.grid()
    plt.show()
