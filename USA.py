import matplotlib.pyplot as py
import matplotlib.patches as patch
base = patch.Rectangle((0,0), width=120, height=67.5, facecolor="white", edgecolor="#000000")
corner = patch.Rectangle((0,35), width=60, height=32.5, facecolor="#0000FF", edgecolor="#000000")
m,n = py.subplots()
n.add_patch(base)
n.add_patch(corner)
n.add_artist(py.text(20, 70, "United States of America", fontdict=None, c="#0000FF", size=20))
i = 60
for num in range(0, 35, 5):
   n.add_patch(patch.Rectangle((0,num), width=120, height=2.5, facecolor="red", edgecolor="#000000"))
for num in range(35, 70, 5):
   n.add_patch(patch.Rectangle((60,num), width=60, height=2.5, facecolor="red", edgecolor="#000000"))
for j in range(0, 4):
   for num in range(5, 65, 10):
      n.add_artist(py.text(num, i, "*", fontdict=None, c="white", size=10))
   i = i - 2.5
   for num in range(10, 60, 10):
      n.add_artist(py.text(num, i, "*", fontdict=None, c="white", size=10))
   i = i - 2.5   
for num in range(5, 65, 10):
   n.add_artist(py.text(num, 40, "*", fontdict=None, c="white", size=10))
py.axis("equal")
py.savefig("USA.png")
print("Figure saved!")