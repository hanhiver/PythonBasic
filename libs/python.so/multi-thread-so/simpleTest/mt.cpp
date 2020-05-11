#include <iostream>
#include <vector>
#include <thread>

using namespace std;

extern "C"
{

void testlib()
{
    cout << "Lib load OK!" << endl;
}

void run()
{
	int i = 10;
    std::cout << "Thread ID: " << std::this_thread::get_id() << std::endl;
	while (--i)
	{
		std::this_thread::sleep_for(chrono::milliseconds(10));
		cout<<"i= "<<i<<std::endl;
	}
}

void StartThread(int th_number)
{
    /*
    thread th1(run);
    thread th2(run);
    th1.join();
    th2.join();
    */
    
    vector<thread> threads; 

    for (int i=0; i<th_number; ++i)
    {
        thread th = thread(run);
        threads.push_back(std::move(th));
    }
    
    for (int i=0; i<th_number; ++i)
    {
        threads[i].join();
    }
}


int main()
{
    /*
	thread th1(run);
	thread th2(run);
	th1.join();
	th2.join();
    */
    StartThread(3);
	return 0;
}

} // extern "C"

