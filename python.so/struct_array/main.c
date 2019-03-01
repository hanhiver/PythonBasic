#include <stdio.h>
#include "test.h"

int main()
{
    struct Point plist[3];
    testlib();

    genPoint(plist, 3);
    readPoint(plist, 3);

    return 0;
}

