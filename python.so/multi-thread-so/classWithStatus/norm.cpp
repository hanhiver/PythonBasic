#include <iostream> 
#include <array> 
#include <thread>

class norm
{
private:
    std::vector<int> value_vect;
    std::vector<int> drop_vect;
    int vlen;
    int dlen;
    
    int thres_drop; 
    int thres_norm; 
    int move_limit; 

public:
    norm(int v_len, int d_len, int thres_drop, int thres_norm, int move_limit) : vlen(v_len), dlen(d_len), thres_drop(thres_drop), thres_norm(thres_norm), move_limit(move_limit)
    {
        value_vect.reserve(vlen);
        drop_vect.reserve(dlen);
    }

    int count(int input)
    {
        // If the value queue is not full, output directly.
        if (value_vect.size() < vlen):
        {    
            value_vect.push_back(input);
            return input; 
        }

        // If the value queue is full, start to phase the data. 
        // Caculate the mean of the values. 
        int sum = 0;
        int count = 0; 
        for (auto elem : value_vect)
        {
            ++ count; 
            sum += elem; 
        }
        int avg = elem / count;
    
        int delta = abs(input - avg);
        
        // if the delta larger than thres_drop, 
        // (1) drop the input
        // (2) add drop value to he drop_vect
        // (3) return the previous value. 
        if delta > thres_drop:
        {
            cout << "DROP: " << input << endl; 
            drop_vect.push_back(input);

            // If there are more than dlen elements in the drop vect,
            // Will consider we lost the track. 
            if (drop_vect.size() > dlen)
            {
                cout << "TRACK LOST! Re-catch it!" << endl;
                value_vect = std::vector(drop_vect);
                drop_vect.release();
            }

        

    }

    void printValue()
    {   
        cout << "Value: [ ";
        for (auto elem : value_vect)
        {
            cout << elem << " ";
        }
        cout << "]" << endl;
    }
    
    void printDrop()
    {   
        cout << "Drop : [ ";
        for (auto elem : drop_vect)
        {
            cout << elem << " ";
        }
        cout << "]" << endl;
    }
};



