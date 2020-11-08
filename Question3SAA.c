#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <mpi.h>
#include "timer.h"
#include <string.h>


int main(int argc, char* argv[])
{
  MPI_Init(&argc, &argv);
  int rank;
  int num_procs;	
  MPI_Comm_rank(MPI_COMM_WORLD, &rank);	
  MPI_Comm_size(MPI_COMM_WORLD, &num_procs);
  MPI_Status recv_status;
  double* times = (double*)malloc(26 * sizeof(double));
  double start, end;

  for (int i = 0; i < 26; i++)
  {
    int x = pow(2, i);
    if (i < 6)
    {
      x = 64;
    }
    double* arr = (double*) malloc(x * sizeof(double));	
    double* firstHalf = (double*)malloc((x/2) * sizeof(double));
    double* secondHalf = (double*)malloc((x/2) * sizeof(double));
    if(rank == 0) 
    {
      for(int k = 0; k < x; k++) 
      {
	arr[k] = k * 1.0;
      }
    }
    int numberOfProcesses = num_procs;
    int size = (int)log2(num_procs);
    start = get_time();
    for(int j = 0; j < size; j++) 
    {
      if((rank % numberOfProcesses) == 0)
      {
	int middle = x/2;
	memcpy(firstHalf, arr, middle * sizeof(double));
	memcpy(secondHalf, &arr[middle], middle * sizeof(double));
	int send = rank + (numberOfProcesses/2);
        MPI_Send(secondHalf, x/2, MPI_DOUBLE, send, 1234, MPI_COMM_WORLD);
	arr = (double*) realloc (arr, (x/2) * sizeof(double));
      }
      else if((rank + (numberOfProcesses/2)) %numberOfProcesses == 0)
      {
	int receive = rank - (numberOfProcesses/2);
	arr = (double*) realloc (arr, (x/2) * sizeof(double));
        MPI_Recv(arr, x, MPI_DOUBLE, receive, 1234, MPI_COMM_WORLD, &recv_status);
      }
      numberOfProcesses = numberOfProcesses/2;
      x = x/2;
      firstHalf = (double*) realloc (firstHalf, x/2 * sizeof(double));
      secondHalf = (double*) realloc (secondHalf, x/2 * sizeof(double));
    }
    double dummy = 0;
    
    for(int i = 0; i < num_procs; i++) 
    {
      if(rank != 0)
      {
	MPI_Recv(&dummy, 1, MPI_DOUBLE, rank - 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
      }
      MPI_Send(&dummy, 1, MPI_DOUBLE, (rank + 1) % num_procs, 0, MPI_COMM_WORLD);
      if(rank == 0)
      {
	MPI_Recv(&dummy, 1, MPI_DOUBLE, num_procs - 1, 0, MPI_COMM_WORLD, MPI_STATUS_IGNORE);
      }
    }
    if(rank == 0)
    {
      end = get_time();
      times[i] = get_seconds(start, end);
    }
  }	
  if(rank == 0)
  {
    for (int q = 0; q < 26; q++)
    {
      printf("i = %d, time = %e\n", q, times[q]);
    }
  }
  MPI_Finalize();
  return 0;	
}
