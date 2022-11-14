"""
Created on Thu Nov 10 08:43:22 2022

    ______________________________
                GreeDS - DEMO
    ______________________________

GreeDS algorithm from Pairet etal 2020.
Basic implemented that works independently from MAYONNAISE.
Nov 14 : Added r_start to improve results
Require the dependancy torch and kornia

@author: sand-jrd
"""

from GreeDS import GreeDS
from vip_hci.fits import open_fits, write_fits
from vip_hci.preproc import cube_crop_frames

dir = "your_directory"

cube = open_fits(dir+"your_cube.fits")#[my_channel] # Must be one channel cube 
angles = open_fits(dir+"your_PA_angles.fits")

r = 20  # Iteration over PCA-rank
l = 20  # Iteration per rank
r_start = 10 # PCA-rank to start iteration
pup_size = 6 # Raduis of numerical mask to hide coro

full_output = False  # If True, return every iterations. Better if you are searching optimized param

# Crop you cube (optional)
crop_size = 200
cube = cube_crop_frames(cube, crop_size)

res = GreeDS(cube, angles, r=r, l=l, r_start=r_start, pup=pup_size, full_output=True)
write_fits(dir+"GreeDS_estimation_"+str(r)+"_"+str(l)+"_"+str(r_start), res)
