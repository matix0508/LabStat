from operator import inv
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np
from typing import List
from uncertainties import ufloat

def inverse_square(x, a):
    return a/x**2


class CurveFit:
    def __init__(self, x: np.ndarray, y: np.ndarray, func: 'function', parameters: List[str]) -> None:
        self.x = x
        self.y = y
        self.func = func
        self.parameters = parameters
        self.output = {}
        self.popt = None
        self.pcov = None

    def find_curve(self):
        self.popt, self.pcov = curve_fit(self.func, self.x, self.y)
        for i, parameter in enumerate(self.parameters):
            self.output[parameter] = ufloat(self.popt[i], self.pcov[i])
        
    def plot(self):
        xdata = np.linspace(self.x.min(), self.x.max(), 100)
        plt.scatter(self.x, self.y)
        plt.plot(xdata, self.func(xdata, self.output['a'].nominal_value))
        plt.show()

# popt, pcov = curve_fit(inverse_square, xdata, ydata)
