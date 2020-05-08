#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int testlib()
{
    printf("Test OK inside lib.\n");
    return 0;
}


int wbuf(void* buf, int bufsize)
{
    char* string = "Handong!";
    char* pos = (char*)buf; 

    int i = 0; 
    
    if (bufsize < strlen(string))
    {
        printf("Buffer size too small. \n");
        return -1;
    }

    for (i=0; i<strlen(string); i++)
    {
        pos[i] = string[i];
    }

    printf("Write buf finished.\n");
    
    return i; 
}

int rbuf(void* buf, int bufsize)
{
    char string[bufsize];
    char* pos = (char*)buf;

    int i = 0;
    
    for (i=0; i<bufsize; i++)
    {
        string[i] = pos[i];
    }

    printf("Read buf finished. \n");
    printf("buf content: \"%s\" \n", pos);

    return i;
}

int matrix_write(void* buf, int strides[], int shapes[])
{
    int i, j, M, N, s0, s1;
    int* pos = (int*)buf;

    printf("Input buf %p. \n", buf);

    M = shapes[0];
    N = shapes[1];
    s0 = strides[0] / sizeof(int);
    s1 = strides[1] / sizeof(int);

    printf("Initialize the matrix: %p \n", buf);

    int init_value = 1; 

    for (i=0; i<M; i++)
    {
        for (j=0; j<N; j++)
        {
            pos[i*s0 + j*s1] = init_value++; 
            printf("(%d, %d) : %d \n", i, j, pos[i*s0 + j*s1]);
        }
    }

    printf("Initialize Done! \n");

    return 0;
}

int matrix_add(void* buf, int strides[], int shapes[])
{
    int sum = 0;
    int i, j, M, N, s0, s1;

    int* pos = (int*)buf;

    M = shapes[0];
    N = shapes[1];
    s0 = strides[0] / sizeof(int);
    s1 = strides[1] / sizeof(int);

    printf("Add all items in the matrix: %p \n", buf);

    for (i=0; i<M; i++)
    {
        for (j=0; j<N; j++)
        {
            sum += pos[i*s0 + j*s1];
            printf("(%d, %d) : %d \n", i, j, pos[i*s0 + j*s1]);
        }
    }

    printf("Sum of the matrix is: %d. \n", sum);

    return 0; 
}

int create_matrix(void** buf, int size)
{
    printf("Create %d buf in create_matrix. \n", size);

    *buf = (void*)malloc(size);
    if (NULL == *buf)
    {
        printf("malloc failed! \n");
        return -1;
    }

    printf("Create buf %p OK. \n", *buf);

    return 0;
}

int main()
{   
    printf("=== String Test ===\n");
    void* buf1 = NULL;
    buf1 = (void *)malloc(20);

    if (NULL == buf1)
    {
        printf("malloc failed! \n");
        return -1;
    }

    wbuf(buf1, 20);
    rbuf(buf1, 20);
    
    free(buf1);

    printf("String Test Done! \n\n");

    printf("=== Matrix Test ===\n");
    void* buf2 = NULL;
    printf("buf2 before: %p \n", buf2);
    
    /*
    buf2 = (void *)malloc(6 * sizeof(int));
    if (NULL == buf2)
    {
        printf("malloc failed! \n");
        return -1;
    }*/

    create_matrix(&buf2, 6*sizeof(int));
    printf("buf2 after: %p \n", buf2);

    int strides[2]; 
    strides[0] = 3 * sizeof(int);
    strides[1] = 1 * sizeof(int);

    int shapes[2];
    shapes[0] = 2;
    shapes[1] = 3;

    matrix_write(buf2, strides, shapes);
    matrix_add(buf2, strides, shapes);

    free(buf2);

    return 0;
}


