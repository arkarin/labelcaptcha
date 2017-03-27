# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from PIL import Image
import matplotlib.pyplot as plt

import os

srcdir = './unlabel/'
dstdir = './label/'

flist = os.listdir(srcdir)
fcont = len(flist)

stidx = len(os.listdir(dstdir))

for fidx in range(fcont):
    fulldir = srcdir + flist[fidx]
    im = Image.open(fulldir)
    plt.imshow(im)
    plt.show()
    lbstr = raw_input("Input the label of image (input 'EXIT' to end):")
    if lbstr == 'exit' or lbstr == 'EXIT':
        print "exit..."
        break
    lbstr = str(lbstr)
    stridx = str(fidx + stidx).zfill(4)
    newdir = dstdir + stridx + '_' + lbstr + '.jpg'
    
    im.save(newdir)
    os.remove(fulldir)
    
print "All the files have been labeled!"
