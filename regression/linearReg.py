import numpy as np

from regression.regressionModel import Model


class linearReg(Model):
    def __init__(self, dim: int) -> None:
        super().__init__()
        self.dim = dim
        self.w = np.zeros(shape=(dim + 1, 1))

    def fit(self, x, y):
        S = np.dot(np.transpose(m.w), m.w)
        S = np.linalg.pinv(S)

        self.w = np.dot(np.transpose(x), y)
        self.w = np.dot(S, self.w)
        print('Fitting finished')

        pass

    def predict(self, x):
        return np.dot(self.w, x)

    def showParas(self):
        print(f'w = \n{self.w}')
