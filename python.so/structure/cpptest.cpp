#include<iostream>

using namespace std;

//该文件名称：cpptest.cpp

//终端下编译指令：

//g++ -o cpptest.so -shared -fPIC cpptest.cpp

struct sub_struct{
    char* test_char;
    int test_int;
};

struct struct_def {
    char* stru_string;
    int stru_int;
    char stru_arr_num[4];
    sub_struct son_struct;
};

extern "C"
{//在extern “C”中的函数才能被外部调用

    int test(struct_def  struct_mystruct, struct_def* struct_test_p) 
    {
        //输出结构体指针的数据
        cout<<"输出结构体中的char*字符:";
        cout << struct_mystruct.stru_string << endl;
        cout<<"输出结构体中的int型：";
        cout << struct_mystruct.stru_int <<endl;
        cout <<"输出结构体中的字符数组:";

        for(int x = 0; x< 4; x++)
            {
                cout << struct_mystruct.stru_arr_num[x]<<"   ";
            }

        cout<< endl;
        cout<<"输出子结构体中的char*型：";
        cout << struct_mystruct.son_struct.test_char<<endl;
        cout<<"输出子结构体中的int型：";
        cout<<struct_mystruct.son_struct.test_int<<endl;

        //输出结构体指针的数据
        cout<<endl;
        cout<<endl;
        cout<<"输出结构体指针中的char*字符:";
        cout << struct_test_p->stru_string << endl;
        cout<<"输出结构体指针中的int型：";
        cout << struct_test_p->stru_int <<endl;
        cout <<"输出结构体指针中的字符数组:";

        for(int x = 0;x< 4;x++)
            {
                cout << struct_test_p->stru_arr_num[x]<<"   ";
            }

        cout<< endl;
        cout<<"输出子结构体指针中的字符串：";
        cout<<struct_test_p->son_struct.test_char;
        cout << endl;
        cout<<"输出子结构体指针中的int型：";
        cout<<struct_test_p->son_struct.test_int<<endl;
    }
}
