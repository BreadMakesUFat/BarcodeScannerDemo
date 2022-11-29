#include <stdlib.h>
#include <stdio.h>

int main ()
{
    int exit = 0;

	exit = system("git reset --hard HEAD");
    if (exit) printf("git reset failed!");

    exit = system("git pull");
    if (exit) printf("git pull failed!");

	return 0;
}