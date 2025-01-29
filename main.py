import random as r
import os

def main(L,seed,filename,num_loops):
    with open(f"{filename}.f90",'w') as f:
        # Header
        f.write("use , intrinsic :: iso_fortran_env, only: sp=>real32 , dp=>real64, compiler_version, compiler_options\n")
        f.write("implicit none\n")
        f.write("real(dp), external :: rkiss05\n")
        f.write(f"real(dp) :: J({L-1})\n")
        f.write("integer :: i\n")

        # declaration of temporary variables and loop variables
        string = ""
        for i in range(num_loops):
            string += f"real(dp) :: r{i}\ninteger :: i{i}\n"
        f.write(string)
        
        # setting J array with random variables
        f.write(f"call kissinit({seed})  ! put seed. call with r = rkiss05()\n")
        #string = "J(:) = 1_dp\n"  # just for testing
        string = f"do i = 1,{(L-1)}\nJ(i) = rkiss05()**2\nend do\n"
        f.write(string)

        # loops 
        string = f"r0 = 0_dp\ndo i0 = 1,{L-1}\n"
        for i in range(1,num_loops):
            string += f"r{i} = 0_dp\n"
            string += f"do i{i} = (i{i-1} + 2),{L - 1}\n"
        f.write(string)
        
        string = f"r{num_loops-1} = r{num_loops-1} + J(i{num_loops-1})\nend do\n"
        for i in range(num_loops-1,0,-1):
            string += f"r{i} = r{i} * J(i{i-1})\n"
            string += f"r{i-1} = r{i-1} + r{i}\nend do\n"
        f.write(string)

        # to write results
        f.write(f'open(2,file="output_{filename}.txt", action="write")\n')
        f.write('write(2,*) "# Compiler version = ", compiler_version()\n')
        f.write('write(2,*) "# Compiler flags = ", compiler_options()\n')
        f.write(f'write(2,*) "# L = ", {L}\n')
        f.write(f'write(2,*) "# seed = ", {seed}\n')
        f.write(f'write(2,*) "# Result = ", r0\n')
        f.write("close(2)\n")
        f.write("end\n")

if __name__ == "__main__":
    seed = 12
    filename = "resposta"
    L = 48
    num_loops = int((L- 6)/2)   # -4 or -6 or not. Might have to change this.
    print("Setting up file...")
    main(L,seed,filename,num_loops)
    print("Compiling...")
    os.system(f"gfortran {filename}.f90 rkiss05.o -o {filename} -Ofast")
    print("Running...")
    os.system(f"./{filename}")
    os.system(f"cat output_{filename}.txt")
