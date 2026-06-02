def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    # convert the into its simpler derivative (2ax + b)

    for _ in range(steps):
        gd = 2*a*x0 + b # derivative 
        x0 = x0 - lr*gd # update
    return x0