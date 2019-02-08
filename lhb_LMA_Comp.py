"""
Landon Buell
Lightning Research
Game Plan Take 11
37 Feb 2019
"""
   
            #################
            #### IMPORTS ####

import lhb_LMA_Base as Base
import numpy as np
import os

            ###################################
            #### COMPOSITE LEVEL FUNCTIONS ####

def Initialize ():
    """
    Initializes full script
    --------------------------------
    Return dictionary of directories
    """
    int_dir = os.getcwd()                           # establish initial directory
    
            #### Enter & Test Reading Directory Path ####
    while True:                                     # Setup to establish a reading directory
        #read = Base.Input_Directory('READ FROM')    # accept user input
        read = 'C:/Users/Landon/Documents/Lightning Research/data_rawINTF_201-400'
        path = Base.Change_Directory(read)          # attempt to change path       
        if path == True:                            # if successful,
            break                                   # break the loop
   
            #### Enter & Test Reading Directory Path ####
    while True:                                     # Setup to establish a reading directory
        #write = Base.Input_Directory('WRITE TO')    # accept user input
        write = 'C:/Users/Landon/Documents/Lightning Research/INTF_201-400'
        path = Base.Change_Directory(write)         # attempt to change path
        if path == True:                            # if successful,
            break                                   # break the loop
        else:                                       # if failure (path DNE)
            path = Base.Input_Create_Directory()    # prompt user to create path
            if path == True:                        # if yes,
                os.mkdir(write)                     # make the directory
                break

            #### Sub-Directory Paths ####
    paths = Base.Make_Sub_Dirs(write)               # create sub paths and dictionary to store them
    paths['readdir'] = read                         # add read dir to paths dictionary
    paths['intdir'] = int_dir                       # add int dir to paths dictionary
    paths['writedir'] = write                       # add write dir to paths dictionary
    return paths                                    # return dictionary of needed directories

