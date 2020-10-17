#include <stdlib.h>
#include <stdio.h>
#include "timer.h"
#include <math.h>
#include <mpi.h>
#include <time.h>

// Serial Function for approximating pi
int main(int argc, char* argv[])
{
  MPI_Init(&argc, &argv);
  int rank, num_procs;
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  MPI_Comm_size(MPI_COMM_WORLD, &num_procs);
  long n_samples = pow(2, 20)/num_procs;
  long n_in_circle = 0;
  double rand_x, rand_y;
  double start, end;

  // Seed random number generator
  srand(time(NULL));

  start = MPI_Wtime();
  for (long i = 0; i < n_samples; i++)
  {
     rand_x = (double)(rand()) / RAND_MAX;  // X is between 0 and 1
     rand_y = (double)(rand()) / RAND_MAX;  // Y is between 0 and 1

     // If inside circle, add to n_in_circle
     if ((rand_x*rand_x) + (rand_y*rand_y) <= 1)
       n_in_circle++;
  }
  end = MPI_Wtime() - start;
  int total = 0;
  MPI_Reduce(&n_in_circle, &total, 1, MPI_INT, MPI_SUM, 0, MPI_COMM_WORLD);
  MPI_Reduce(&end, &start, 1, MPI_DOUBLE, MPI_MAX, 0, MPI_COMM_WORLD);

  // Pi is approximately 4 * number in circle / total number in square
  double pi = 4.0*n_in_circle / n_samples;

  if (rank == 0)
  {
    printf("NSamples %ld, Pi Approx %e\n", n_samples, pi);
    printf("Elapsed Time %e\n", start);
  }

  MPI_Finalize();
  return 0;
}
