#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <mpi.h>
#include "timer.h"

int main(int argc, char* argv[])
{
  MPI_Init(&argc, &argv);
  int rank;
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);
  MPI_Status recv_status;
  double* times = (double*)malloc(19 * sizeof(double));
  double start, end;
  
  for (int i = 0; i < 16; i++) //i should go upto 19, used 2 for testing purposes
  {
    int x = pow(2, i);
    double* size = (double*)malloc(x * sizeof(double)); 
    if (rank == 0)
    {
      for (int k = 0; k < x; k++)
      {
        size[k] = k * 1.0;
      }
      start = get_time();
    }
    
    for (int j = 0; j < 1000; j++)//j should go upto 1000, used 10 for testing purposes
    {
      if (rank == 0)
      {
        MPI_Send(size, x, MPI_DOUBLE, 1, 1234, MPI_COMM_WORLD);
        MPI_Recv(size, x, MPI_DOUBLE, 1, 1234, MPI_COMM_WORLD, &recv_status);
      }
      else if (rank == 1)
      {
        MPI_Recv(size, x, MPI_DOUBLE, 0, 1234, MPI_COMM_WORLD, &recv_status);
        MPI_Send(size, x, MPI_DOUBLE, 0, 1234, MPI_COMM_WORLD);    
      }
    }
    if (rank == 0)
    {
      end = get_time();
      times[i] = get_seconds(start, end);
    }
  }

  if (rank == 0)
  {
    for (int q = 0; q < 16; q++)
    {
      printf("i = %d", q);
      printf(", time = %e\n", times[q]);
    }
  }
  MPI_Finalize();
  return 0;
}
