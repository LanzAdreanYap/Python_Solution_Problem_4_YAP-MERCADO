import matplotlib.pyplot as p
import numpy as np
from math import *

#input
yi = float(input("The initial height of the projectile above the ground in meters (m): "))
v = float(input("The magnitude of the velocity in m/s: "))
A = float(input("The angle in degrees with respect to the +x-axis at which the projectile is fired: "))
ax = float(input("The acceleration in the x-component in m/s^2: "))
ay = float(input("The acceleration in the y-component in m/s^2: "))

if ay == 0: #set the condition where the input y-acceleration is invalid if ay == 0
    print(' ')
    print("Your acceleration in the y-component is invalid.")
elif A > 180 or A < 0: #set the condition where the input angle is invalid if angle is less than 0 or greater than 180
    print(' ')
    print("The input angle was invalid")
else:
    ###########CALCULATIONS
    
    #FOR NON-IDEAL MOTION
    
    #Velocity in x
    vxi = float(v*cos(A * pi/180)) 
    #Velocity in y
    vyi = float(v*sin(A * pi/180)) 
    
    #Time based on y
    #Using y = vyi*t -(1/2)*ay*(t^2) ; y = -y1
    a = -(1/2)*ay
    b = vyi
    c = yi
    #Get its roots
    tfinal = np.roots([a,b,c])
    #Get only the positive time
    tf = tfinal.max(axis=0)
    
    #Create time interval 0 - tf
    t = np.linspace(0,tf,1000)
    
    #x and y for plotting
    x = vxi*t+(1/2)*ax*t*t
    y = yi + vyi*t-(1/2)*ay*t*t


    #FOR IDEAL MOTION
    
    #Same vxi and vyi
    #Acceleration of yc component is 9.8 and no acceleration for x component
    
    #Time based on y
    #Using y = vyi*t -(1/2)*g*(t^2) where y = -y1
    #Use quadratic formula to get the time
    aid = -4.9
    bid = vyi
    cid = yi
    #Get its roots
    tfinalid = np.roots([aid,bid,cid])
    #Get only the positive time
    tfid = tfinalid.max(axis=0)
    
    #Create time inter 0 - tf
    tid = np.linspace(0,tfid,1000)
    
    #xid and yid for plotting
    xid = vxi*tid
    yid = yi + vyi*tid-(4.9)*tid*tid
    
    
    #Plotting
    p.subplot(1,2,1)
    p.plot(x,y)
    p.xlabel('x distance (m)')
    p.ylabel('y distance (m)')
    p.title('For Non-Ideal Motion')
    p.axis('equal')
    
    
    p.subplot(1,2,2)
    p.plot(xid,yid)
    p.xlabel('x distance (m)')
    p.ylabel('y distance (m)')
    p.title('For Ideal Motion')
    p.axis('equal')