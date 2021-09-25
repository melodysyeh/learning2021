import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from matplotlib.patches import Polygon


fig, ax = plt.subplots(subplot_kw={'aspect': 'equal'})

ax.add_artist(Ellipse((0, 0), 4, 2, angle=0, alpha=0.1))
ax.add_artist(Ellipse((0, 1), 4, 2, angle=0, alpha=0.1))
ax.add_artist(Polygon(np.array([[1,2], [2,5], [1.5,1]]), closed=False))

ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)

plt.show()
