#include <stdio.h>
#include <stdlib.h>
#include "timer.h"

int main(int argc, char *argv[])
{
  //Read n
  long num = strtol(argv[1], NULL, 10);
  int n = num;
  //  printf("%d\n", n);
  
  //declaration of matrix and vectors to be used. B holds the matrix-vector multiplication
  double* X = (double*)malloc(n*sizeof(double));
  double* A = (double*)malloc(n*n*sizeof(double));
  double* B = (double*)malloc(n*sizeof(double));

  //Initialization of the vecotrs
  for (int i = 1; i <= n; i++)
  {
    X[i-1] = 1.0;
    B[i-1] = 0;
  }

  //Initializationof the matrix
  for(int i = 1; i <= n*n; i++)
  {
    A[i-1] = 1.0/i;
  }
  
  double start = get_time();

  //matrix-vector multiplication
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < n; j++)
    {
      B[i] = B[i] + (A[(i*n)+j]*X[j]);
    }
  }

    
  double end = get_time();

  double seconds = get_seconds(start, end);

  printf("Seconds: %e\n", seconds);

  //In case results need to be printed
  /*for (int i = 0; i < n; i++)
  {
    printf("%.6f\n", B[i]);
  }
  */

}
