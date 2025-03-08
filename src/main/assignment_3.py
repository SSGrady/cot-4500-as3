import numpy as np

def euler_method(func, t_range, initial_val, iterations):
    """Euler Method for approximating solutions to Ordinary Differential Equations."""
    t_min, t_max = t_range
    h = (t_max - t_min) / iterations
    t = t_min
    y = initial_val

    for _ in range(iterations):
        y += h * func(t, y)
        t += h

    # Return approximation of y at t_max.
    return y

def runge_kutta_method(func, t_range, initial_val, iterations):
    """Runge-Kutta Method for approximating solutions to Ordinary Differential Equations."""
    t_min, t_max = t_range
    h = (t_max - t_min) / iterations
    t = t_min
    y = initial_val

    for _ in range(iterations):
        k1 = h * func(t, y)
        k2 = h * func(t + h/2, y + k1/2)
        k3 = h * func(t + h/2, y + k2/2)
        k4 = h * func(t + h, y + k3)

        y += 1/6 * (k1 + 2*k2 + 2*k3 + k4)
        t += h

    # Return approximation of y at t_max.
    return y

if __name__ == '__main__':
    # Parameters
    func = lambda t, y: t - y**2
    t_range = (0, 2)
    initial_val = 1
    iterations = 10

    # Solve using Euler's Method
    euler_result = euler_method(func, t_range, initial_val, iterations)
    print(f"Euler Method Result: {euler_result}")

    # Solve using Runge-Kutta Method
    runge_kutta_result = runge_kutta_method(func, t_range, initial_val, iterations)
    print(f"Runge-Kutta Method Result: {runge_kutta_result}")