#include <stdio.h>
#include <stdlib.h>
#include "timer.h"

int main()
{
  //Matrix size is 1K by 1K
  int n = 1000;

  //declaration of matrices to be used. C holds the matrix matrix multiplication solution
  double* A = (double*)malloc(n*n*sizeof(double));
  double* B = (double*)malloc(n*n*sizeof(double));
  double* C = (double*)malloc(n*n*sizeof(double));

  //Initializationof the matrices
  for(int i = 1; i <= n*n; i++)
  {
    A[i-1] = 1.0/i;
    B[i-1] = 1.0;
    C[i-1] = 0;
  }
  double val;

  double start = get_time();
  
  //matrix-matrix multiplication
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < n; j++)
    {
      val = A[(i*n)+j];
      for (int k = 0; k < n; k++)
      {
	C[(i*n)+k] += val * B[(j*n)+k];
        //printf("%.6f\n", C[(i*n)+k]);
      }
    }
  }

  double end = get_time();

  double seconds = get_seconds(start, end);

  printf("Seconds: %e\n", seconds);

  //in case results need to be published
  /*
  for(int l = 0; l < n*n; l++)
  {
    printf("%.6f\n", C[l]);
  }  
  */
}
