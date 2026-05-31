import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    y = np.asarray(x)
    denominator = 1 + np.exp(-y)
    return 1 / denominator 
    
    pass