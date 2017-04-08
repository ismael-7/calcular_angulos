#! /usr/bin/python
from math import *
l1=1
l2=1
x=1.414213
y=0.0
r2=pow(x,2)+pow(y,2)
aux=r2-pow(l1,2)-pow(l2,2)
cosBeta=-aux/(float) (2*l1*l2)
aux=1-pow(cosBeta, 2)
senoBeta=sqrt(aux)
beta=0.0
if cosBeta!=0:
    beta=atan(senoBeta/cosBeta)
else:
    beta=asin(senoBeta)
beta=pi+beta

aux= -pow(l2,2)+pow(l1,2)+r2
cosAlpha=aux/(2*l1*sqrt(r2))
aux=1-pow(cosAlpha, 2)
senoAlpha=sqrt(aux)
alpha=0.0
if cosAlpha!=0:
    alpha=atan(senoAlpha/cosAlpha)
else:
    alpha=asin(senoAlpha)

gama=0.0
if r2!=0:
    gama=asin(y/sqrt(r2))
else:
    gama=0
alpha=gama+alpha
beta=pi-beta
print (alpha,beta)