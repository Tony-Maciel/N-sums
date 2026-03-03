/*
 * Given an integer from the CLI (e.g. N), this program calculates all the combinations 
 * the N-dimensional vector (x_0, x_1, ..., x_{N-1}) can yield, where x_i = 0, 1, ..., N-1.
 *
 * NOTE: usage: execute this program and give it ONE integer in the command line.
 * */

#include <stdio.h>
#include <stdlib.h>

void all_combinations(int depth, int N, int *vec) {
  if (depth == N) { // found combination
    printf("(");
    for (int j = 0; j < N-1; ++j)
      printf("%d, ", vec[j]);
    printf("%d)\n", vec[N-1]);

  } else { 
    for (int i = 0; i < N; ++i) { // could replace N here with another integer to generalize program .. 
      vec[depth] = i;             // ... This would make x_i = 0, 1, ..., L-1.
      all_combinations(depth + 1, N, vec);
    }
  }

}

int main(int argc, char **argv) {
  // a couple check to prevent core dumps...
  if (argc > 2) {
    printf("Give ONLY one nonzero integer argument.\n");
    return 1;
  }

  if (argc < 2) {
    printf("Give a single nonzero integer argument.\n"); 
    return 1;
  }

  int N = atoi(argv[1]); // converts string "x" to x, where x is a positive integer

  if (N == 0) { 
    printf("Give NONZERO integer argument.\n");
    return 1;
  }

  int *vec = malloc(sizeof(int) * (N-1));   
  all_combinations(0, N, vec);
  free(vec);

  return 0; 
}
