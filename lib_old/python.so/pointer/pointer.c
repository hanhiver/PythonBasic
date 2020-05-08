#include <stdio.h>

typedef struct TestPointer
{
	int a;
	char* b;
}testpointer;

testpointer* test(testpointer* t)
{
	t->a = t->a + t->a;
	printf("%d\n%s\n", t->a, t->b);
	return t;
}

