use , intrinsic :: iso_fortran_env, only: sp=>real32 , dp=>real64, compiler_version, compiler_options
implicit none
real(dp), external :: rkiss05
real(dp) :: result
integer :: i0
integer :: i1
integer :: i2
integer :: i3
integer :: i4
integer :: i5
integer :: i6
integer :: i7
integer :: i8
result = 0.0_dp
do i0 = 1,9
do i1 = 1,9
do i2 = 1,9
do i3 = 1,9
do i4 = 1,9
do i5 = 1,9
do i6 = 1,9
do i7 = 1,9
do i8 = 1,9
result = result + 1.0_dp
end do
end do
end do
end do
end do
end do
end do
end do
end do
open(2,file="output_nested.txt", action="write")
write(2,*) "# Compiler version = ", compiler_version()
write(2,*) "# Compiler flags = ", compiler_options()
write(2,*) "# Result = ", result
close(2)
end
