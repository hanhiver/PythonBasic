#include "test.h"

int main()
{
	struct MOUSE test_m; 
	test_m.right = 1; 
	test_m.left = 2;

	struct COMPUTER test_c; 
	test_c.my_screen = 3;
	test_c.my_mouse = test_m;

	test();
	read(&test_c);
	job(test_c);

	return 0;
}

