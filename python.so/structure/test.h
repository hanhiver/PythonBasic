#include <stdio.h>

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

int job(computer comp);

int test();

