"""
Landon Buell
Lightning Research
Game Plan Take 11
7 Feb 2019
"""

            #################
            #### IMPORTS ####

import lhb_LMA_Base as Base
import lhb_LMA_Comp as Comp
import numpy as np
import os

            ######################
            #### USER PAHSE I ####

def PHASE_I ():
    """
    Phase I serves to initalize the program. All starting paramters are
    inputted or defaulted to here. 
    """
    paths = Comp.Initialize()                   # Dictionary of important paths
    filelist = Base.Extract_Files(paths['readdir'],'.txt')
    print("\nThere are",len(filelist),"files in the requested directory path.")
    print("Expected Computation time:")
    print("Between",int((len(filelist)*0.5)),\
        "and",int((len(filelist)*0.8)),"seconds")

    return paths,filelist
