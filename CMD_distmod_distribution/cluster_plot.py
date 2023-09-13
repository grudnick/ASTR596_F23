from matplotlib import pyplot as plt
import numpy as np
#from astropy.io import ascii
from astropy.io.votable import parse_single_table

def cmdplot(clustname='', magshift=0,colshift=0):

    path = 'Project_clusters/'

    #read in target cluster
    filename = path + clustname + ' 20arcmin-result.vot'
    table = parse_single_table(filename)
    cldat = table.array

   #read in target cluster
    filename = path + 'M 45 20arcmin-result.vot'
    table = parse_single_table(filename)
    refcldat = table.array

    #read in pleiades
    #reffilename = path + 'pleiadesdata.txt'
    #refcldat = ascii.read(reffilename)

    #set plotting parameters
    plotsize_single=(9,7)
    params = {'backend': 'pdf',
                  'axes.labelsize': 18,
                  'font.size': 18,
                  'legend.fontsize': 12,
                  'xtick.labelsize': 14,
                  'ytick.labelsize': 14,
                  #'lines.markeredgecolor'  : 'k',  
                  #'figure.titlesize': 20,
                  'mathtext.fontset': 'cm',
                  'mathtext.rm': 'serif',
                  #'text.usetex': True,
                  'figure.figsize': plotsize_single}
    plt.rcParams.update(params)

    #apply Vthe magnitude offset
    Vshift = cldat['phot_rp_mean_mag'] + magshift
    BVshift = cldat['bp_rp'] + colshift

    #plot clusters
    plt.plot(BVshift, Vshift, 'ko',markersize=3,alpha=0.8, label=clustname)
    plt.plot(refcldat['bp_rp'], refcldat['phot_rp_mean_mag'], 'ro',markersize=3,alpha=0.8, label = 'Pleiades')
    plt.ylim(18, 2)
    plt.xlim(-0.5, 3.5)
    plt.xlabel('GBP-GRP')
    plt.ylabel('GRP')
    plt.title(clustname)
    plt.legend(loc='upper left')

    s = 'Magnitude Shift =  %.2f'%(magshift)
    scol = 'Color Shift =  %.2f'%(colshift)

    plt.text(1.5, 4,s, horizontalalignment='left',fontsize=20)
    plt.text(1.5, 3,scol, horizontalalignment='left',fontsize=20)

    plt.show()
        
