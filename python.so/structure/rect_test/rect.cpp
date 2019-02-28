#include <iostream>

struct Point
{
	int x;
	int y;
};

struct Rect
{
	int deep;
	Point lt;
	Point rb;
};

extern "C"
{
	int test()
	{
		std::cout<<"Test OK from lib. "<<std::endl;
		return 0;
	}

	int printPoint(Point p)
	{
		std::cout<<"POINT: "<<std::endl;
		std::cout<<"X = "<<p.x<<" Y = "<<p.y<<std::endl;
		return 0;
	}

	int printRect(Rect r)
	{
		std::cout<<"RECT:  "<<std::endl;
		std::cout<<"DEEP = "<<r.deep<<std::endl;
		printPoint(r.lt);
		printPoint(r.rb);
		return 0;
	}

}