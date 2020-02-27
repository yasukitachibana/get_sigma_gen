### get_sigma_gen.py
This is the code to extract sigmaGen() and sigmaErr() from test_dat.out files of JETSCAPE and generate files storing them.
The names of test_dat.out files must have the form of ```TestOutBin*_*.out```. 

To run code, type

  ```
  python get_sigma_gen.py [name of dirctory where you put test_dat.out files]
  ```
  
If you do not specify the name of the directory for the 1st argument in the command, the code trys to find test_dat.out files in the current directory.

The generated Sigma files are saved in the same directory as the test_dat.out files and their names have the form of ```SigmaHardBin*_*.out```.
