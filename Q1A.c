#include <stdio.h>
#include <stdlib.h>
#include "timer.h"

int main()
{
  //Matrix size is 1K by 1K
  int n = 1000;

  //declaration of matrices to be used. C holds the matrix matrix multiplication solution
  float* A = (float*)malloc(n*n*sizeof(float));
  float* B = (float*)malloc(n*n*sizeof(float));
  float* C = (float*)malloc(n*n*sizeof(float));

  //Initializationof the matrices
  for(int i = 1; i <= n*n; i++)
  {
    A[i-1] = 1.0/i;
    B[i-1] = 1.0;
    C[i-1] = 0;
  }

  double start = get_time();

  //matrix-matrix multiplication
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < n; j++)
    {
      for (int k = 0; k < n; k++)
      {
	C[(i*n)+k] += A[(i*n)+j] * B[(j*n)+k];
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
