"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import numpy as np
import matplotlib.pyplot as plt

# parabola parameters
g = 9.81
v0 = 5
h = 1
u = 1/np.sqrt(1+2*g*h/v0**2) # u = tg theta
xmax = v0**2/g/u
us = np.asarray([ np.tan(-np.pi/2/9), np.tan(np.pi/3), u, np.tan(np.pi/2 * 7/8), np.tan(np.pi/2*95/100) ])
ts = np.arctan(us) * 180 / np.pi
ylab = [ 'θ = ' + '%.1f'%t + '°' for t in ts]
ymax = v0**2/g*np.sin(np.max(ts)*np.pi/180)

# functions
x = np.arange(0,2*xmax,0.01)
ys = [ - g/2/v0**2 * (1+u**2) * x**2 + u * x + h for u in us]

# plot
fig, ax = plt.subplots()
ax.set_xlim([0, 1.1*xmax])
ax.set_ylim([-.2, 1.1*ymax])
[ plt.plot(x,y,label=l) for y,l in zip(ys,ylab) ]
plt.legend()
plt.grid(linestyle='--')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('$v_0 = ' + '%.2f'%v0 + '\\, m/s \\quad \\theta_{max} = ' + '%.2f'%ts[2] + '^\\circ \\quad x_{max} = ' + '%.2f'%xmax + '\\, m$')
plt.savefig("parabolic-range.png")
#plt.show()
