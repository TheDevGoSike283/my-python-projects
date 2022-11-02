import numpy as np
import matplotlib.pyplot as py
import matplotlib.patches as patch
a = patch.Rectangle((0,1), width=96, height=16, facecolor='green', edgecolor='#000000')
b = patch.Rectangle((0,17), width=96, height=16, facecolor='white', edgecolor='#000000')
c = patch.Rectangle((0,33), width=96, height=16, facecolor='#FF6103', edgecolor='#000000')
d = patch.Rectangle((0,-121), width=5, height=122, facecolor='grey', edgecolor='#000000')
e = patch.Ellipse((5,-115), width=150, height=12, facecolor='green', edgecolor='#000000')
m,n = py.subplots()
n.add_patch(a)
n.add_patch(b)
n.add_patch(c)
n.add_patch(d)
n.add_patch(e)
radius=6.4
py.plot(48,25, marker='o', markerfacecolor = '#000088ff', markersize = 9.5)
chakra = py.Circle((48,25), radius, color = '#000088ff', fill=False, linewidth=7)
n.add_artist(chakra)
for i in range(0,24):
   p = 48 + radius/2 * np.cos(np.pi*i/576 + np.pi/2304)
   q = 48 + radius/2 * np.cos(np.pi*i/576 - np.pi/2304)
   r = 25 + radius/2 * np.sin(np.pi*i/576 + np.pi/2304)
   s = 25 + radius/2 * np.sin(np.pi*i/576 - np.pi/2304)
   t = 48 + radius * np.cos(np.pi*i/96)
   u = 25 + radius * np.sin(np.pi*i/96)
   n.add_patch(patch.Polygon([[48,25], [p,r], [t,u],[q,s]], fill=True, closed=True, color='#000088ff'))
py.axis('equal')
py.savefig('indian_flag.png')
