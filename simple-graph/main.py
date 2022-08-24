import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


def get_ticks_labels(ticks):
    result = []
    for tick in ticks:
        if tick % 1 == 0:
            result.append(tick)
        else:
            result.append(None)
    return result

if __name__ == "__main__":
# https://matplotlib.org/stable/tutorials/introductory/customizing.html#runtime-rc-settings
    mpl.rcParams['lines.linewidth'] = 2
    mpl.rcParams['lines.linestyle'] = '--'
    x = [0, 1, 2, 3, 4, 5]
    y = [2, 3, 4, 8, 1, 2.3]
    fig, ax = plt.subplots()
    #https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xticks.html
    locs, labels = plt.xticks()  # Get the current locations and labels.
    ticks = np.arange(0, len(x), step=0.5)
    ticks_labels = get_ticks_labels(ticks)
    #breakpoint()
    plt.xticks(ticks, ticks_labels)
    plt.grid(color="black", linestyle="-", linewidth=0.1)
    ax.plot(x, y)
    #fig.show()
    fig.savefig("result.png")

