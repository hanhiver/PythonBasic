#include <stdio.h>

struct Point
{
	int x;
	int y;
};

struct Rect
{
	int deep;
	struct Point lt;
	struct Point rb;
};

int test()
{
	printf("Test OK from lib. \n");

	return 0;
}

int printPoint(struct Point p)
{
	printf("POINT:  \n");
	printf("X = %d Y = %d \n", p.x, p.y);

	return 0;
}

int printRect(struct Rect r)
{
	printf("RECT:   \n");
	printf("DEEP = %d \n", r.deep);
	printPoint(r.lt);
	printPoint(r.rb);

	return 0;
}

struct Point pointAdd(struct Point a, struct Point b)
{
	struct Point resPoint;
	resPoint.x = a.x + b.x;
	resPoint.y = a.y + b.y;

	return resPoint;
}
