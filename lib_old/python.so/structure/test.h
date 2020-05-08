#include <stdio.h>

struct MOUSE
{
	int right;
	int left;
};

struct COMPUTER
{
	int my_screen;
	struct MOUSE my_mouse;
};

int job(struct COMPUTER comp);
int read(struct COMPUTER* comp);
int test();

