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

int read(struct COMPUTER* comp)
{
	printf("read: right = %d, left = %d, my_screen = %d\n", comp->my_mouse.right, comp->my_mouse.left, comp->my_screen);
	return 0;
}


int job(struct COMPUTER comp)
{	
	printf("job: right = %d, left = %d, my_screen = %d\n", comp.my_mouse.right, comp.my_mouse.left, comp.my_screen);
	int res = (comp.my_mouse.right + comp.my_mouse.left) * comp.my_screen;
	printf("I have a mouse: %d. \n", res);
	return res;
}

int test()
{
	printf("Test OK. \n");
	return 0;
}

