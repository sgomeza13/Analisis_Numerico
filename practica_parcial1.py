import numpy as np
import pandas as pd
import math

x = 6.6
fx = np.log(18)+(x/18) - ((x**2)/648)
fx_menos_uno = np.log(18) + (x/18)
exactitud = abs(np.log(x+18)-fx)
precision = abs(fx - fx_menos_uno)
print(exactitud, "exactitud")
print(precision, "precision")
