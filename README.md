# N-sums
## tldr: Given a number N, this program calculates a specific formula that involves N/2 sums.

### Intro
The program main.py explicitly calculates the equation given below. The central problem is to be able to calculate a variable number of loops not known beforehand. So the program should receive an integer N and calculate N/2 loops. This is a somewhat well known problem and there exist many solutions (many more elegant than the one I present here), but all of which have some degree of overhead (at least all those that I have seen), so their execution time is, in principle, not the best it could be. Naively, I figured this would be a good opportunity to take a stab at this problem and conceptualize a solution with less overhead (It never occured to me that this would not be the brightest idea, because the time complexity of such an algorithm would be at best O(N^N), i.e. , N would only be able to take on values up to like 50 and run in a reasonable amount of time...). 

### Description
The program works in the following way: given an integer N, main.py writes a fortran 90 program with N/2 loops. It writes a header, then declares all the loop variables, then writes the loops and finally makes it so that the result be written to an output file along with compiler specs. All thats left would be to compile and run the fortran file.

### Final remarks
In hindsight, this project probably wasn't the best use of my time, but I thought the final solution was pretty cool, so I decided to post it here. I hope this repository helps somebody in their endeavors one day. My key takeaway from all this was that, statistically speaking, any optimizations I wish to implement probably fall in the 97% of cases...

"There is no doubt that the grail of efficiency leads to abuse. Programmers waste enormous amounts of time thinking about, or worrying about, the speed of noncritical parts of their programs, and these attempts at efficiency actually have a strong negative impact when debugging and maintenance are considered. We should forget about small efficiencies, say about 97% of the time: premature optimization is the root of all evil." - Donald Knuth.
