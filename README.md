# N sums and N combinations
## PROBLEM: Given a number N (not known beforehand), the task is to calculate N nested loops and all the combinations of the N dimensional vector (x_0, x_1, ..., x_{N-1}), where x_i = 0, 1, ..., N-1.

### tl;dr: Two programs have been made, the first is a meta program in python that calculates the N loops explicitely (practically without overhead) by writing, compiling and running a fortran file. The other is a C program that uses recursion to solve the latter problem above.

### Solution 1 (N sums)
My solution to this problem is to write a meta program in python that creates another program (in fortran) with the desired number of loops. In detail, this python program (nestedloops.py), reads the integer N, opens a new fortran file (nested.f90) and writes some boilerplate code required for it, declares the roughly N variables to be used in the loops in this fortran file, writes each loop explicitly, writes code to make the fortran file save the results of the loops in an output file and finally compile and run this fortran file. The actual calculation performed at the heart of all the loops is just a simple increment of an accumulator to count how many iterations of the innermost loop have been performed. The expected result is N^N.

### Solution 2 (N combinations)
My solution to this problem is pretty straightforward, I just use a simple recursive function in C that finds all the desired combinations. The program is called "all_combinations.c".

### Final remarks
I originally encountered the N sums problem as part of a larger one that my friend was working on. I precipitously started working on a solution without ever realizing that the time complexity of such a problem was O(N^N). All I could think about was the best way to solve this problem with as little overhead as possible. Shortly after writing nestedloops.py, in my post fugue state, I was notified that there was a much better way to tackle the larger problem, without having an algorithm that ran in O(N^N) time complexity. It was at that moment that I realized that all my work fell squarely in the 97% of cases...

"There is no doubt that the grail of efficiency leads to abuse. Programmers waste enormous amounts of time thinking about, or worrying about, the speed of noncritical parts of their programs, and these attempts at efficiency actually have a strong negative impact when debugging and maintenance are considered. We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil." - Donald Knuth.

In hindsight, this project probably wasn't the best use of my time, but I thought the final solution was pretty different, so I decided to post it here. My key takeaway from all of this was to think twice before trying to optimize a solution to a problem all willy-nilly. 

As for the N combinations problem, I just decided to add it to this repository because of the similarity it has to the N sums problem. The N combinations problem is actually part of a larger problem that I encountered in my other repository (IC-2025), where I had to implement periodic boundary conditions for a square lattice in N dimensions.
