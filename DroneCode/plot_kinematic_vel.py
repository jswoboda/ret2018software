from tkinter import Tk                      # to get window and select file.
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

import sys                                  # to kill program when needed.

import os                                   # to run instruction in the bash.

import pandas                               # to manipulate csv files.

import math                                 # to use sin and cos

import numpy                                # to use numpyarrays

import pyproj                               # library that does coordinate
                                            # transformations.

import matplotlib as mpl                    # to plot data.
from mpl_toolkits.mplot3d import Axes3D
mpl.use("TKAgg")         ### Uncomment this line to use framework TKAgg
# That will be a temporary solution. Trying the files before:
# Use it becuase the python is using the wrong frameowrk and gives an error.
# Creating the following .matplotlib/matplotlibrc file seem to solve the problem:
# Downloaded a sample file that only contains uncommented the following line:
#               backend : TKAgg
# The file is in the folder ~/.matplotlib and it has extension .dms
# That doesn't solve the problem.
# I added the same file to the anaconda matplotlib folder.
# /anaconda3/lib/python3.6/site-packages/matplotlib/
# Didn't work either... so I just have to add that line with TKAgg framework...
# Solution maybe here: https://www.codesofinterest.com/2018/05/fixing-matplotlib-pyplot-import-errors.html

import matplotlib.pyplot as plt


def plot_velocity3D_vector(time_coordinates):        # input=numpyArray

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.plot(time_coordinates[:,1], time_coordinates[:,2], time_coordinates[:,3], color='red', label='parametric curve + velocity vector')

    for n in range(0,numpy.size(time_coordinates,0)-1,10):
        ax.quiver(time_coordinates[n,1], time_coordinates[n,2], time_coordinates[n,3],time_coordinates[n,4], time_coordinates[n,5], time_coordinates[n,6], color='blue')

    ax.legend()
    ax.set_aspect('equal', adjustable='box')

    plt.show()

def plot_velocity3D_vector_ENU(time_coordinates):        # input=numpyArray

    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ax.plot(time_coordinates[:,1], time_coordinates[:,2], time_coordinates[:,3], color='red', label='trajectory TLP + velocity vector')

    for n in range(0,numpy.size(time_coordinates,0)-1,10):
        ax.quiver(time_coordinates[n,1], time_coordinates[n,2], time_coordinates[n,3],time_coordinates[n,4], time_coordinates[n,5], time_coordinates[n,6], color='blue')

    ax.legend()
    ax.set_aspect('equal', adjustable='box')

    ax.set_xlabel('x_local or EAST')
    ax.set_ylabel('y_local or NORTH')
    ax.set_zlabel('z_local or UP')
    plt.show()


if __name__ == '__main__':

# This main program is just for testing purposes. That's why the labeling of the columns.
# Could be used to plot any coordinates in Cartesian system, if you lable columns appropriately.
    print("Select .CSV file to plot. Make sure the file contains columns with headers the form: timestamp, x_local-E, y_local-N, z_local-U, vel_x, vel_y, vel_z")

    Tk().withdraw() # we don't want the full GUI, this keeps the root window
                        # from appearing.
    fileName=askopenfilename()

    extension=fileName[len(fileName)-3::]    # gets extension

    if extension=='csv' or extension!='CSV':
        pass
    else:
        print('Wrong extension of file, try again...')
        sys.exit()

    # read the csv file into variable DataFrame (This is for files processed with
    # our own software, labled "CLEAN"; If it is a random CSV file, won't read the right columns
    # or you labled them by hand x_local-E,y_local-N,z_local-U)
    colnames=['timestamp','x_local-E','y_local-N','z_local-U','vel_x','vel_y','vel_z']
    df=pandas.read_csv(fileName,usecols=colnames) # df is of the type DataFrame.

    posvel=df.to_numpy(copy=True)           # returns a ndarray (Numpy-array,
                                                # NOT a Numpy-matrix). Options for columns= list, optional.

    plot_velocity3D_vector_ENU(posvel)
