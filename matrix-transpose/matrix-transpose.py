import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # the lazy way ;)
    # return np.transpose(A)
    
    A = np.asarray(A)
    m, n = A.shape
    A1 = np.zeros((n,m),dtype=A.dtype)

    for i in range(m):
        for j in range(n):
            A1[j][i] = A[i][j]
    return A1

    