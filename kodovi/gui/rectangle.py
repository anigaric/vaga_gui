import matplotlib.pyplot as plt
import matplotlib
# matplotlib.rcParams['toolbar'] = 'None'

f, (ax1) = plt.subplots(1,1,figsize=(2,2))
f.subplots_adjust(hspace=0,wspace=0)

# ***** Make 2 rectangles and add it to the figure ********* #
width = 2
len = 4
rect1 = matplotlib.patches.Rectangle((0, 0), width, len, linewidth=2, edgecolor='k', facecolor='none')
ax1.add_patch(rect1)

rect2 = matplotlib.patches.Rectangle((5, 0), width, len, linewidth=2, edgecolor='k', facecolor='none')
ax1.add_patch(rect2)


ts = ax1.transData
coords = [1, 2]                                                                                   #tocka oko koje se rotira pravokutnik
tr = matplotlib.transforms.Affine2D().rotate_deg_around(coords[0],coords[1], 10)
t = tr + ts

coords2 = [6, 2]                                                                                   #tocka oko koje se rotira pravokutnik
tr2 = matplotlib.transforms.Affine2D().rotate_deg_around(coords2[0],coords2[1], -10)
t2 = tr2 + ts

# ****** Rotate rectangles and add it to the figure ****** #
rect1_rot = matplotlib.patches.Rectangle((0, 0), width, len, linewidth=1, edgecolor='r', facecolor='none', transform=t)
ax1.add_patch(rect1_rot)

rect2_rot = matplotlib.patches.Rectangle((5, 0), width, len, linewidth=1, edgecolor='r', facecolor='none', transform=t2)
ax1.add_patch(rect2_rot)

# ******** Figure settings ****** #
plt.grid(True)
plt.axis('off')
# plt.title("Zakret stopala")
ax1.set_xlim(-1, 8)
ax1.set_ylim(-1, 5)

plt.show()