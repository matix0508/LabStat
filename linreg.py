from typing import Tuple

import statsmodels.api as sm
from uncertainties import ufloat
import numpy as np

class LinReg:
    def __init__(self, x: np.ndarray, y: np.ndarray) -> None:
        self.x = x
        self.y = y
        self.model = None
        self.results = None
        self.a = None
        self.b = None

        self.setup()
        

    def setup(self) -> None:
        self.x = sm.add_constant(self.x)
        self.model = sm.OLS(self.y, self.x)
        self.results = self.model.fit()
        self.a, self.b = self.get_a_b()



    def get_a_b(self) -> Tuple[ufloat]:
        a = self.results.params[1]
        b = self.results.params[0]
        ua = self.results.bse[1]
        ub = self.results.bse[0]
        a = ufloat(a, ua)
        b = ufloat(b, ub)
        return (a, b)

    def __repr__(self) -> str:
        return f"y = ({self.a:.2e})x + ({self.b:.2e})"
    


    
