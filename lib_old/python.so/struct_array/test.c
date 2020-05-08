#include <stdio.h>

struct Point
{
    int x; 
    int y;
};

int testlib()
{
    printf("Test OK from lib. \n");
    return 0;
}


int genPoint(struct Point* plist, int num)
{
    int i = 0;
    for (i=0; i<num; i++)
    {
        plist[i].x = i;
        plist[i].y = i;
    }

    return 0;
}

int readPoint(struct Point* plist, int num)
{
    int i = 0;
    for (i=0; i<num; i++)
    {
        printf("Point[%d]: x = %d, y = %d. \n", i, plist[i].x, plist[i].y);
    }

    return 0;
}

