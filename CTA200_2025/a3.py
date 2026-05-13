import numpy as np


def bounded_and_diverging():
    N=1000 
    x=np.linspace(-2,2,N)
    y=np.linspace(-2,2,N)

    x,y=np.meshgrid(x,y) # now each is a 1000^2 matrix
    c=x+1j*y # make a complex plane

    z=np.zeros(c.shape, dtype=int) # copy of c with zeros
    # stores information about complex plane
    bounded = np.ones(c.shape, dtype=bool) #t/f - has diverged or not
    # diverging = np.ones(c.shape) # stores the iteration index for diverging
    diverging = np.full(c.shape, 1000, dtype=float) 


    for i in range(1000): # NOTE: maybe get rid of this
        z=z**2+c # vectorized calculation of z[i,j] * z[i,j] + c[i,j]
        diverged = np.abs(z)>2 # if greater than 2, maps to false, less maps to true for 1000^2 grid each iter

        newly_div = diverged & bounded # points that are currently diverged and not bounded

        diverging[newly_div] = i # diverged at iteration i
        bounded[newly_div] = False # did not diverge

    return bounded, diverging
