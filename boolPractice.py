import pandas as pd
import numpy as np

array = np.arange(10)
print(array)
populations = {"Ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6}, "Nevada": {2001: 2.4, 2002: 2.9}}
frame = pd.DataFrame(populations)


un = (frame['Ohio'].unique())
print(sorted(un))