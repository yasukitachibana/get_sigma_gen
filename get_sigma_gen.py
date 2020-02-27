##
## README
## To run code, type
##  $python get_sigma_gen.py [name of dirctory where you put test_dat.out files]
## If you do not specify the name of the directory for the 1st argument in the command
## The code trys to find test_dat.out files in the current directory.
## The generated Sigma files are saved in the same directory as the test_dat.out files
##









import os
import glob as glob
import sys
import numpy as np



def Main(argc,argvs):

    dir = os.getcwd()
    if argc > 1:
        dir = argvs[1]
    
    print('generate sigmaGen file from *.out files in '+dir)

    ###################################################################
    ### Here you can specify the name of test_dat.out file
    get_dot_out_list = glob.glob('TestOutBin*_*.out')
    ###################################################################

    print(get_dot_out_list)

    for dot_out_file in get_dot_out_list:
        with open(dot_out_file, mode='r') as f:
            lines = f.readlines()
        lines = [line.strip() for line in lines]
        l_sigma_gen = [line for line in lines if 'sigmaGen' in line]
        l_sigma_err = [line for line in lines if 'sigmaErr' in line]
        
        val_sigma_gen = l_sigma_gen[-1].split()[-1]
        val_sigma_err = l_sigma_err[-1].split()[-1]
    
        simga_out_filename = 'SigmaHardBin' + dot_out_file.split('Bin')[-1]

        print('generating: '+simga_out_filename)
        print('sigma = ' , val_sigma_gen,' +/- ',val_sigma_err)
        
        data = val_sigma_gen +' '+val_sigma_err+'\n'
        
        simga_out_file = open(simga_out_filename,'w')
        simga_out_file.write(data)
        simga_out_file.close

        print('-')



if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)
    Main(argc,argvs)
