"""
Landon Buell
Lightning Research
Game Plan Take 11
7 Feb 2019
"""

            #################
            #### IMPORTS ####

import mas_raw
import numpy as np
import matplotlib.pyplot as plt
import os 

            ##############################
            #### USER INPUT FUNCTIONS ####

def Input_Directory (text):
    """
    Accept user input to identify a directory path
    -------------------------------
    text (str) : text to complete a input question sentence
    -------------------------------
    returns a user inputted directory path
    """
    while True:
        try:
            path = str(input("\nPlease enter the directory you wish to "+text+" : "))
            if not path:
                print("\n\tERROR! - Please input a directory")
            if path == ' ':
                print("\n\tERROR! - Please input a value")
            else:
                return path
                break
        except:
            print("\n\tERROR! - Inavlid value type")

def Input_Create_Directory ():
    """
    Accept user confirmation to create a firectory path
    -------------------------------
    path (str): directory path to create if desired
    -------------------------------
    returns True/False if yes/no respectivly
    """
    yes = ['y','yes','Y','YES']
    no = ['n','no','N','NO']
    while True:
        try:
            path = str(input("\nCreate this directory path?: "))
            if not path:
                print("\n\tERROR! - Please input a value!")
            if path in yes:
                return True
                break
            if path in no:
                return False
                break
            else:
                print("\n\tERROR! - That input is not valid")
        except:
            print("\n\tERROR! - Inavlid value type")

            ##############################
            #### PRINT , PLOT & GRAPH ####

def Process_Times(int,fin,num):
    """
    Print Out timing data for program
    -------------------------------
    int (float) : inital script time reading
    fin (float) : final script time reading
    num (int) : number of files processed
    """
    print("\n",'-'*64)
    print("Process time for",num,"files:")
    print("\t",(fin-int),"seconds")
    print("Averaged",((fin-int)/num),"seconds per file")

def Single_Graph(x_data,y_data,title,save=False,show=False):             
    """
    Save a .png file of a plot  of 1 list for external use
    -------------------------------
    x_data (array): list to serve as the x-values for the plot
    y_data (array): list to serve as the y-values for the plot
    title (str): title of the plot an name to save as
    save (bool): Save plot to current directory as .png if True. False by default
    show (bool): Show plot of the current figure if True. False by default
    -------------------------------
    """
            ### Initialize ###
    plt.figure(figsize=(16,12))                     # set figure & size
    plt.ticklabel_format(style='sci',\
                axis='x', scilimits=(0,0))          # Sci notation on x-axis
    plt.title(title,fontsize=36,fontweight='bold')  # add title
    plt.xlabel("Data Index",\
        fontsize=20,fontweight='bold')              # label x-axis
    plt.ylabel("E-Feild Amp [V/m]",\
        fontsize=20,fontweight='bold')              # label y-axis
            ### Recreate Indices for X-axis ###
    plt.plot(x_data,y_data,color='purple')          # plot the dataset
    plt.grid(True)                                  # Create gridlines
    if save == True:                                # if the plot wants to be saved
        plt.savefig(title+'.png')                   # save the event figure
    if show == True:                                # if the plot wants to be shown
        plt.show()                                  # display the plot
    plt.close()                                     # close the figure

def Change_Directory (directory):
    """
    Attempt to change working directory path
    -------------------------------
    directory (str) : directory to attempt a change to
    -------------------------------
    returns True/False for success/failure respectivly
    """
    try:                                        # Attempt
        os.chdir(directory)                     # change the path
        print("\n\tSuccessfully changed Directory paths")
        return True                             # return True
    except:                                     # if fails
        print("\n\tERROR! - Could not change directory path!")
        return False                            # return False

def Extract_Files (directory,extension):
    """
    Find all files of a certain extension in a given directory path
    -------------------------------
    directory (str) : full directory path to seach given file types for
    extension (str) : indicated the desired file types to search for
    -------------------------------
    Returns a list of files (str) that contains all the files the designated type 
    """
    filelist = []                                   # Empty list to store filenames
    for root, dirs, files in os.walk(directory):    # elements in directory
        for file in files:                          # in those elements           
            if file.endswith(extension):            # If desired file type
                filelist.append(file)               # add to list of files           
    return filelist                                 # Return the list of files

def Make_Sub_Dirs (path):
    """
    Creates a series of directories within a specified path
    -------------------------------
    path (str) : parent directory to create paths within
    -------------------------------
    returns a dictionary of of sub directory paths
    """
            #### Create all Sub dirs ####
    passplots = path+'/NBEs/Plots'
    passarrays = path+'/NBEs/Arrays'
    failplots = path+'/Non-NBEs/Plots'
    failarrays = path+'/Non-NBEs/Arrays'
    paths = [passplots,passarrays,failplots,failarrays]
    
    for path in paths:                  # for each directory path
        try:                            # try to create path:
            os.makedirs(path)           # make the path (And other dirs)
        except:                         # if failure,
            pass                        # do nothing

    dict = {'passplots':passplots,
            'passarrays':passarrays,    
            'failplots':failplots,
            'failarrays':failarrays}    # create a dictionary of directory paths
    return dict                         # return the dictionary

