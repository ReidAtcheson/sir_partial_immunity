import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import sir

#Example script running the simulation

N=100000.0
rho=1.0
beta=1.75
gamma=0.5
omega=0.01
delta=2*gamma
psi=beta

ts=np.linspace(0,2000,2000)
S,I,R,PS,PI=sir.sir(N,rho,beta,gamma,omega,delta,psi,ts,[N-1,1.0,0.0,0.0,0.0])

plt.plot(I+PI)
plt.savefig("test.svg")
