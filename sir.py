import numpy as np
from scipy.integrate import odeint
Sid=0
Iid=1
Rid=2
PSid=3
PIid=4
def sir(N,rho,beta,gamma,omega,delta,psi,ts,y0):
    def fn(xs,t):
        S=xs[Sid]
        I=xs[Iid]
        R=xs[Rid]
        PS=xs[PSid]
        PI=xs[PIid]
        ys=np.zeros(len(xs))
        ys[Sid ]=-(rho*beta*(I+PI)/N) * S
        ys[Iid ]= (rho*beta*(I+PI)/N) * S - gamma*I
        ys[Rid ]=                           gamma*I - omega*R                            + delta*PI
        ys[PSid]=                                     omega*R - (rho*psi*(I+PI)/N) * PS
        ys[PIid]=                                               (rho*psi*(I+PI)/N) * PS  - delta*PI
        
        return ys
    res=odeint(fn,y0,ts)
    S =np.array(list(map(lambda x : x[Sid ],res)))
    I =np.array(list(map(lambda x : x[Iid ],res)))
    R =np.array(list(map(lambda x : x[Rid ],res)))
    PS=np.array(list(map(lambda x : x[PSid],res)))
    PI=np.array(list(map(lambda x : x[PIid],res)))
    return S,I,R,PS,PI
