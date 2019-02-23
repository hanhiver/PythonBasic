#include <stdio.h>
#include "test.h"

/*
typedef struct MOUSE
{
	int right;
	int left;
} mouse;

typedef struct COMPUTER
{
	int my_screen;
	mouse my_mouse;
} computer;
*/

int job(computer comp)
{	
	printf("right = %d, left = %d, my_screen = %d\n", comp.my_mouse.right, comp.my_mouse.left, comp.my_screen);
	int res = (comp.my_mouse.right + comp.my_mouse.left) * comp.my_screen;
	printf("I have a mouse: %d. \n", res);
	return res;
}

int test()
{
	printf("Test OK. \n");
	return 0;
}

