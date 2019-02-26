#include <iostream> 

using namespace std;

struct sub_struct
{
	int test_int1;
	int test_int2;
};

struct struct_def 
{
	int test_int3;
	sub_struct son_struct;
};

extern "C"
{
	int test_value(struct_def mystruct)
	{
		cout<<"Pass Value test: "<<endl;
		cout<<"test_int3: "<<mystruct.test_int3<<endl;
		cout<<"test_int1: "<<mystruct.son_struct.test_int1<<endl;
		cout<<"test_int2: "<<mystruct.son_struct.test_int2<<endl;
		
	}

	int test_pointer(struct_def* mystruct_p)
	{
		cout<<"Pass pointer test: "<<endl;
		cout<<"test_int3: "<<mystruct_p->test_int3<<endl;
		cout<<"test_int1: "<<mystruct_p->son_struct.test_int1<<endl;
		cout<<"test_int2: "<<mystruct_p->son_struct.test_int2<<endl;
		
	}

}
