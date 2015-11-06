from __future__ import division
from visual import*
from math import e

import math

scene.width = 500
scene.height = 500

scene.autoscale = 0
scene.range = (35,35,35)
scene.center = (12,0,14)
area=box(pos=(12,0,14),length=400,height=400,width=400,material=materials.plastic,color=(.5,.5,.5))
pweight=1.67e-27
ewieght=9.11e-31
fcharge=1.6e-19
enot=8.85e-12
pnot=1.26e-6
clc=8.99e9
count=0


electron=sphere(pos=vector(0,0,11),radius=.8,color=color.blue,material=materials.emissive)

wire=curve(pos=[(24,0,10),(24,0,0),(0,0,0),(0,0,28),(24,0,28),(24,0,18)],radius=.5,material=materials.chrome,color=(1,.7,.3))

plate1=box(pos=(24,0,10),length=10,height=10,width=.1,material=materials.blazed)
plate1charge=box(pos=(24,0,10.8),length=10,height=10,width=1.8,material=materials.shiny,color=color.blue,opacity=(0))
plate2=box(pos=(24,0,18),length=10,height=10,width=.1,material=materials.blazed)
plate2charge=box(pos=(24,0,17.2),length=10,height=10,width=1.8,material=materials.shiny,color=color.red,opacity=(0))
battery=frame()
cylinder(frame=battery,pos=(0,0,10),axis=(0,0,.2),radius=1.5,color=color.blue,material=materials.emissive)
cylinder(frame=battery,pos=(0,0,10.2),axis=(0,0,7.8),radius=1.5,color=color.green)
cylinder(frame=battery,pos=(0,0,12),axis=(0,0,7),radius=.75,color=color.red,material=materials.emissive)


cfield1 = arrow(pos=(20,4,18), axis=(0,0,0), shaftwidth=.3)
cfield2 = arrow(pos=(24,4,18), axis=(0,0,0), shaftwidth=.3)
cfield3 = arrow(pos=(28,4,18), axis=(0,0,0), shaftwidth=.3)
cfield4 = arrow(pos=(20,-4,18), axis=(0,0,0), shaftwidth=.3)
cfield5 = arrow(pos=(24,-4,18), axis=(0,0,0), shaftwidth=.3)
cfield6 = arrow(pos=(28,-4,18), axis=(0,0,0), shaftwidth=.3)
cfield7 = arrow(pos=(20,0,18), axis=(0,0,0), shaftwidth=.3)
cfield8 = arrow(pos=(24,0,18), axis=(0,0,0), shaftwidth=.3)
cfield9 = arrow(pos=(28,0,18), axis=(0,0,0), shaftwidth=.3)



equilibribox1=box(pos=(24,0,23),length=5,height=5,width=0, opacity=(0))
equilibribox2=box(pos=(24,0,5),length=5,height=5,width=0, opacity=(0))
stop=0
velocity1=vector(0,0,-1)
velocity2=vector(1,0,0)
velocity3=vector(0,0,1)
velocity4=vector(-1,0,0)

scene.waitfor('click')

V = input('-=This will default to 1 if less than or equal to zero=-\nWhat is the battery voltage? ')
if (V<=0):
    V=1
Vc=V
Rw = input('\n-=This will default to .01 ohms if less than that value=-\nwhat is the total system resistance? ')
if (Rw<.01):
    Rw=.01
C = input('\n-=This will be converted to micro Farads=-\nWhat is the capacatance of the capacitor? ')
C=C*10e-6
rt = 1
sp = input('\nRate boost? ')
if (sp<=0):
    sp=1
Q=0
I=(V-(Q/C))/Rw
t=0

label1=label(pos=(0,0,10.2), text='Battery', xoffset=17, yoffset=17)
label2=label(pos=(24,0,10), text='Capacitor', xoffset=47, yoffset=47)
label3=label(pos=(0,0,5), text='Wire', xoffset=47, yoffset=47)

scene.waitfor('click')

electron.pos=(0,0,5)
wfield2 = arrow(pos=(24,0,1), axis=(0,0,4), shaftwidth=1, opacity=(.5), fixedwidth = True)
wfield3 = arrow(pos=(24,0,19), axis=(0,0,4), shaftwidth=1, opacity=(.5), fixedwidth = True)
label1.text='EMF Battery'
label1.pos=(24,0,1)
label2.text=''
label2.pos=(500,500,500)
label2.radius=500
label3.text='Electron'

scene.waitfor('click')

label1.pos=(500,500,500)
label1.radius=500
label3.pos=(500,500,500)
label3.radius=500
electron.pos=(0,0,11)
wfield1 = arrow(pos=(24,0,9), axis=(0,0,0), shaftwidth=1, opacity=(.5), fixedwidth = True)
wfield4 = arrow(pos=(24,0,27), axis=(0,0,0), shaftwidth=1, opacity=(.5), fixedwidth = True)



while Q <= (C*.99*V):
    while electron.pos != (0,0,0):
        rate (I*sp)
        electron.pos=electron.pos+velocity1*1
    while electron.pos != (24,0,0):
        rate (I*sp)
        electron.pos=electron.pos+velocity2*1
    while electron.pos != (24,0,10):
        rate (I*sp)
        electron.pos=electron.pos+velocity3*1
    plate1.color=(0,0,.5)
    plate2.color=(.5,0,0)
    cfield1.axis=(0,0,-1)
    cfield2.axis=(0,0,-1)
    cfield3.axis=(0,0,-1)
    cfield4.axis=(0,0,-1)
    cfield5.axis=(0,0,-1)
    cfield6.axis=(0,0,-1)
    cfield7.axis=(0,0,-1)
    cfield8.axis=(0,0,-1)
    cfield9.axis=(0,0,-1)
    wfield1.axis=(0,0,-1)
    wfield4.axis=(0,0,-1)
    if (Q>C*.1*V):
        plate1.color=(0,0,.6)
        plate2.color=(.6,0,0)
        plate1charge.opacity=(.1)
        plate2charge.opacity=(.1)
        cfield1.axis=(0,0,-3)
        cfield2.axis=(0,0,-3)
        cfield3.axis=(0,0,-3)
        cfield4.axis=(0,0,-3)
        cfield5.axis=(0,0,-3)
        cfield6.axis=(0,0,-3)
        cfield7.axis=(0,0,-3)
        cfield8.axis=(0,0,-3)
        cfield9.axis=(0,0,-3)
        wfield1.axis=(0,0,-2)
        wfield4.axis=(0,0,-2)
    if (Q>C*.2*V):
        plate1.color=(0,0,.7)
        plate2.color=(.7,0,0)
        plate1charge.opacity=(.2)
        plate2charge.opacity=(.2)
        cfield1.axis=(0,0,-4)
        cfield2.axis=(0,0,-4)
        cfield3.axis=(0,0,-4)
        cfield4.axis=(0,0,-4)
        cfield5.axis=(0,0,-4)
        cfield6.axis=(0,0,-4)
        cfield7.axis=(0,0,-4)
        cfield8.axis=(0,0,-4)
        cfield9.axis=(0,0,-4)
        wfield1.axis=(0,0,-2.5)
        wfield4.axis=(0,0,-2.5)
    if (Q>C*.4*V):
        plate1.color=(0,0,.8)
        plate2.color=(.8,0,0)
        plate1charge.opacity=(.3)
        plate2charge.opacity=(.3)
        cfield1.axis=(0,0,-5)
        cfield2.axis=(0,0,-5)
        cfield3.axis=(0,0,-5)
        cfield4.axis=(0,0,-5)
        cfield5.axis=(0,0,-5)
        cfield6.axis=(0,0,-5)
        cfield7.axis=(0,0,-5)
        cfield8.axis=(0,0,-5)
        cfield9.axis=(0,0,-5)
        wfield1.axis=(0,0,-3)
    if (Q>C*.6*V):
        plate1.color=(0,0,.9)
        plate2.color=(.9,0,0)
        cfield1.axis=(0,0,-6)
        cfield2.axis=(0,0,-6)
        cfield3.axis=(0,0,-6)
        cfield4.axis=(0,0,-6)
        cfield5.axis=(0,0,-6)
        cfield6.axis=(0,0,-6)
        cfield7.axis=(0,0,-6)
        cfield8.axis=(0,0,-6)
        cfield9.axis=(0,0,-6)
        wfield1.axis=(0,0,-3.5)
        wfield4.axis=(0,0,-3.5)
    if (Q>C*.8*V):
        plate1.color=(0,0,1)
        plate2.color=(1,0,0)
        plate1charge.opacity=(.5)
        plate2charge.opacity=(.5)
        cfield1.axis=(0,0,-8)
        cfield2.axis=(0,0,-8)
        cfield3.axis=(0,0,-8)
        cfield4.axis=(0,0,-8)
        cfield5.axis=(0,0,-8)
        cfield6.axis=(0,0,-8)
        cfield7.axis=(0,0,-8)
        cfield8.axis=(0,0,-8)
        cfield9.axis=(0,0,-8)
        wfield1.axis=(0,0,-4)
        wfield4.axis=(0,0,-4)
    electron.pos=(24,0,19)
    while electron.pos != (24,0,28):
        rate (I*sp)
        electron.pos=electron.pos+velocity3*1
    while electron.pos != (0,0,28):
        rate (I*sp)
        electron.pos=electron.pos+velocity4*1
    if (Q<C*.96*V):
        while electron.pos != (0,0,12):
            rate (I*sp)
            electron.pos=electron.pos+velocity1*1
        if (rt==False):
            scene.waitfor('click')
        while electron.pos != (0,0,0):
            rate (I*sp)
            electron.pos=electron.pos+velocity1*1
    else:
        while electron.pos != (0,0,12):
            rate (I*sp)
            electron.pos=electron.pos+velocity1*1
            electron.radius=.1
            
    count=count+1
    t=t+(((C*V)/I)/15)
    Vc=V*(e**((-1*t)/(Rw*C)))
    Q=C*V*(1-(e**((-1*t)/(Rw*C))))
    I=(V/Rw)*(e**((-1*t)/(Rw*C)))
    print ('Iteration= ')
    print (count)
    print ('I= ')
    print (I)
    print ('Q= ')
    print (Q)
    print ('Vc= ')
    print (Vc)
    print ('t= ')
    print (t)
    print (e**(-t/(Rw*C)))

equilibribox1.opacity=(1)
equilibribox2.opacity=(1)
label1.pos=(500,500,500)
label1.radius=500
label2.pos=(24,0,14)
label2.text='Electric\nField'
label3.pos=(24,2.5,23)
label3.text='Equilibrium\nReached'
label4=label(pos=((24,-5,18)), text='Surface\nCharge\nDensity', xoffset=-17, yoffset=-17)
scene.waitfor('click')
label2.visible=0
label3.visible=0
label4.visible=0
print ('Simulation complete...')
