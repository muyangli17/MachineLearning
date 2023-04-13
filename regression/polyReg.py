import numpy as np

from regression.regressionModel import Model


class linearReg(Model):
    def __init__(self, degree: int):
        super().__init__()
        self.degree = degree
        self.w = np.zeros(shape=(degree + 1, 1))

    def fit(self, x, y):
        """
        Apply polynomial regression to 1-dimension data (x_i,y_i) with given polynomial degree
        :param x: 1-d independent variable
        :param y: 1-d depedent variable
        :return: parameters of polynomial regression
        """
        pass

    def predict(self, x):
        pass
