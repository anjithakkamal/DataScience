import matplotlib.pyplot as plt
import numpy as np
xpoints = np.array(['mon', 'tues','wed','thurs','fri'])
ypoints = np.array([300,450,150,400,650])
plt.plot(xpoints, ypoints, '*g',ms = 20)
plt.plot(xpoints, ypoints, ':r')

leg = plt.legend(title="Title-Sales Data1 ")
leg._legend_box.align = "right"

plt.show()