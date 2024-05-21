#include<stdio.h>
#include<stdlib.h>

int main()
{
    int *p;
    p = (int *)malloc(256 * 256);
    if(p == NULL)
        printf("Allocation failed");
    return 0;
}