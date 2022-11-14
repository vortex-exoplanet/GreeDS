"""
Created on Thu Nov 10 08:43:22 2022

    ______________________________
                GreeDS - DEMO
    ______________________________

GreeDS algorithm from Pairet etal 2020.
Basic implemented that works independently from MAYONNAISE.
Require the dependancy torch and kornia

@author: sand-jrd
"""

from GreeDS import GreeDS
from vip_hci.fits import open_fits, write_fits

dir = "your_directory"

cube = open_fits(dir+"your_cube.fits")
angles = open_fits(dir+"your_PA_angles.fits")

r = 10  # Iteration over PCA-rank
l = 20  # Iteration per rank
full_output = False  # If True, return every iterations. Better if you are searching optimized param

res = GreeDS(cube, angles, r=r, l=l, full_output=True)
write_fits(dir+"GreeDS_estimation_"+str(r)+"_"+str(l), res)
