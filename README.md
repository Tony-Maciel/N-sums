# N-sums
## tl;dr: Given a number N, this meta program in python calculates N loops explicitely (without overhead) by writing, compiling and running a fortran file.

### Intro
The problem is as follows: write a program that has to perform N total loops (say, from 1 to N), but the catch is that N is an input of your program, so you only know the value of N when the program is running. There are probably many ways to tackle this problem, but all of the solutions that I have seen online involve a considerable amount of overhead. Naively, I figured this would be a good opportunity to take a stab at this problem and conceptualize a solution with less overhead (It never occured to me that this would not be the brightest idea, because the time complexity of such an algorithm would be at best O(N^N), i.e., N would only be able to take on values up to like 50 and run in a reasonable amount of time...). 

### Solution
My solution to this problem is to write a meta program in python that creates another program (in fortran) with the desired number of loops. In detail, in this python program (nestedloops.py), I: read the integer N, open a new fortran file (nested.f90) and write some boilerplate code required for it, declare the roughly N variables to be used in the loops in this fortran file, write each loop explicitly, write code to make the fortran file save the results of the loops in an output file and finally compile and run this fortran file. The actual calculation performed at the heart of all the loops is just a simple increment of an accumulator to count how many iterations of the innermost loop have been performed. The expected result is N^N.

### Final remarks
In hindsight, this project probably wasn't the best use of my time, but I thought the final solution was pretty different, so I decided to post it here. My key takeaway from all of this was to think twice before trying to optimize a solution to a problem all willy-nilly, and that any optimizations I wish to implement probably fall in the 97% of cases...

"There is no doubt that the grail of efficiency leads to abuse. Programmers waste enormous amounts of time thinking about, or worrying about, the speed of noncritical parts of their programs, and these attempts at efficiency actually have a strong negative impact when debugging and maintenance are considered. We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil." - Donald Knuth.
