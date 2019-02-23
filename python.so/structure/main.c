#include "test.h"

int main()
{
	mouse test_m; 
	test_m.right = 1; 
	test_m.left = 2;

	computer test_c; 
	test_c.my_screen = 3;
	test_c.my_mouse = test_m;

	test();
	job(test_c);

	return 0;
}

