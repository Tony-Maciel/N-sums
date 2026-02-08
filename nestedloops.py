import os  # to compile and run the fortran file

def main(filename, num_loops):
    with open(f"{filename}.f90",'w') as f:
        # Header (boilerplate)
        f.write("use , intrinsic :: iso_fortran_env, only: sp=>real32 , dp=>real64, compiler_version, compiler_options\n")
        f.write("implicit none\n")
        f.write("real(dp), external :: rkiss05\n")
        f.write("real(dp) :: result\n")   # accumulator to test if the N loops work

        # declaration of temporary variables and loop variables
        string = ""
        for i in range(num_loops):
            string += f"integer :: i{i}\n"
        f.write(string)
        
        # start N loops 
        string = f"result = 0.0_dp\n"
        for i in range(num_loops):
            string += f"do i{i} = 1,{num_loops}\n"
        f.write(string)
        
        # close N loops
        string = f"result = result + 1.0_dp\n"
        for i in range(num_loops,0,-1):
            string += f"end do\n"
        f.write(string)

        # to write results
        f.write(f'open(2,file="output_{filename}.txt", action="write")\n')
        f.write('write(2,*) "# Compiler version = ", compiler_version()\n')
        f.write('write(2,*) "# Compiler flags = ", compiler_options()\n')
        f.write(f'write(2,*) "# Result = ", result\n')
        f.write("close(2)\n")
        f.write("end\n")

if __name__ == "__main__":
    filename = "nested"
    num_loops = 9
    print("Setting up file...")
    main(filename, num_loops)
    print("Compiling...")
    os.system(f"gfortran {filename}.f90 -o {filename} -O3")
    print("Running...")
    os.system(f"./{filename}")
    os.system(f"cat output_{filename}.txt")
    print(f"expected value = {num_loops**num_loops}")
