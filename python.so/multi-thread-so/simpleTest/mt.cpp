#include <iostream>
#include <thread>

using namespace std;

void run()
{
	int i = 10;
	while (--i)
	{
		std::this_thread::sleep_for(chrono::milliseconds(100));
		cout<<"i= "<<i<<std::endl;
	}
}

int main()
{
	thread th1(run);
	thread th2(run);
	th1.join();
	th2.join();

	return 0;
}
