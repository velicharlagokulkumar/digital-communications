#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

int  main(void) //main function begins
{
 
//Uniform random numbers
gaussian("gau.dat", 1000000);

//Mean of uniform
printf("%lf\n",mean("gau.dat"));

//Mean of uniform
printf("%lf",variance("gau.dat"));
return 0;
}
