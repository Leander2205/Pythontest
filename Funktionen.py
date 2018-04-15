import numpy as np
pi =np.pi
def xi(i,n):
    x= (i-(1.0/2.0)) /n
    return x
def fi(xi,n):
    f=4.0/(1.0+xi**2.0)
    return f
def calc_pi():
    n = 10000
    pi = 0.0
    for i in range(1, n) :
            pi += fi(xi(i, n), n)
    pi /= n

    print ("Eigenes Pi:",pi)
    print ("Numpys PI",np.pi)

calc_pi ()