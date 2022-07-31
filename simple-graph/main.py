import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler

# https://matplotlib.org/stable/tutorials/introductory/customizing.html#runtime-rc-settings

mpl.use('TkAgg')
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'
data = np.random.randn(50)
plt.plot(data)
plt.show()
