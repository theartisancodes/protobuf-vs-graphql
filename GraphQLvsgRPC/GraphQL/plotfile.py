import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
import numpy as np

plt.rcParams.update({
    "lines.color": "white",
    "patch.edgecolor": "white",
    "text.color": "white",
    "axes.facecolor": "white",
    "axes.edgecolor": "lightgray",
    "axes.labelcolor": "white",
    "xtick.color": "white",
    "ytick.color": "white",
    "grid.color": "darkgrey",
    "figure.facecolor": "black",
    "figure.edgecolor": "black",
    "savefig.facecolor": "black",
    "savefig.edgecolor": "black"})

fig = plt.figure()

# use pandas to clean this mess up if you have some spare time

# list of strings
timesstrings = [line.rstrip('\n') for line in open('results.txt')]
# array of strings
timesstringarray = np.asarray(timesstrings)
# array of flaots
timesarray = [float(numeric_string) for numeric_string in timesstringarray]

itterations = len(timesarray)

n, bins, patches = plt.hist(timesarray, bins=1000, density=1, alpha=0.75)
avaragetime = sum(timesarray) / float(len(timesarray))

print("average GraphQL time with keep alive is ", avaragetime)

plt.xlabel("time (miliseconds)")

plt.title("GraphQL keep alive")

plt.axis([0, 1, 0, 25])

plt.grid()

plt.show()