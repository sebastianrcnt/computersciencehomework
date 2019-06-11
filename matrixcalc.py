import numpy as np
from copy import deepcopy
def calcInverse(matrix):  # matrix : np.array(2-d)
    for i in range(len(matrix)):
        assert len(matrix[i]) == len(matrix)

    identityMatrix = []
    for i in range(len(matrix)):
        identityMatrix.append([0]*len(matrix))
        identityMatrix[i][i] = 1
    identityMatrix = np.array(identityMatrix)

    for i in range(len(matrix)):
        # matrix_alias = deepcopy(matrix)
        matrix[i] = matrix[i] / matrix[i][i]
        # identityMatrix[i] = identityMatrix[i] / matrix_alias[i][i]
        for j in range(len(matrix)):
            if i != j:
                # matrix_alias = deepcopy(matrix)
                matrix[j] = matrix[j] - matrix[j][i] * matrix[i]
                # identityMatrix[j] = identityMatrix[j] - matrix_alias[j][i] * matrix_alias[i]

    # for i in range(len(matrix)):
    #     print(f'*** starting column {i+1}')
    #     print(f'dividing row {i+1} with {matrix[i][i]}')
    #     identityMatrix[i] = identityMatrix[i] / matrix[i][i]
    #     matrix[i] = matrix[i] / matrix[i][i]
    #     print(identityMatrix)
    #     for j in range(len(matrix)):
    #         if i != j:
    #             identityMatrix[j] = identityMatrix[j] - matrix[j][i] * identityMatrix[i]
    #             matrix[j] = matrix[j] - matrix[j][i] * matrix[i]
    #             print(identityMatrix)

    return identityMatrix

def calcDet(matrix):
    pass

print(calcInverse(np.array([[1,-1,-1],[3,-1,2],[2,2,3]])))