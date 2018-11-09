import numpy as np
import matplotlib.pyplot as plt

# parameters
g = 9.81
bs = [1,5]
ms = [1,10]
th = np.pi/3
d = 5
v0 = np.sqrt(g*d/np.sin(2*th))
v0x = v0 * np.cos(th)
v0y = v0 * np.sin(th)
xmax=v0**2/g*np.sin(2*th)
ymax=0.5*v0**2/g

# functions
x = np.arange(0,1.1*xmax,0.001)
ys = [
      np.piecewise(x,
                   [ x <= 0, x < m*v0x/b, x >= m*v0x/b ],
                   [ -5 * ymax, lambda x: m**2*g/b**2 * np.log(1 - b*x/(m*v0x)) + v0y / v0x * (1 + m*g/(b*v0y)) * x, -5 * ymax ])
      for b in bs for m in ms]
ylab = [ 'b=' + str(b) + ' m=' + str(m) for b in bs for m in ms]
ypara = -0.5*g/v0x**2* x**2 + v0y / v0x * x

# plot
fig, ax = plt.subplots()
ax.set_ylim([-0.1*ymax, 1.1*ymax])
plt.grid(linestyle='--')
plt.plot(x,ypara, label='parabolic')
[ plt.plot(x,y,label=l) for y,l in zip(ys,ylab)]
plt.legend()
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.title('$\\|\\vec{v}_0\\|$ = '  + '%d.2 m/s'%v0 + ',  $\\theta = ' + str(int(th*180/np.pi + 0.5)) + '^\circ$')
plt.savefig('projectile-friction.png')
