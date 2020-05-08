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
        if (delta > thres_drop)
        {
            cout << "DROP: " << input << endl; 
            drop_vect.push_back(input);

            // If there are more than dlen elements in the drop vect,
            // Will consider we lost the track. 
            if (drop_vect.size() > dlen)
            {
                cout << "TRACK LOST! Re-catch it!" << endl;
                value_vect = std::move(drop_vect);
                drop_vect.clear();
            }

            return avg;
        }

        // if the delta lager than thres_norm,
        // (1) add to value_vect
        // (2) output normalized value
        if (delta > thres_norm)
        {
            cout << "OVERED: " << input << endl;
            // Add the input value to the value_vect. 
            value_vect.push_back(input);
            input = (avg * 2 + input) / 3;
        }

        // Check if the value is in the move_limit range, 
        // if the change is less than move_limit, will not change the output.
        int pre_value = value_vect[value_vect.size()-2];
        if abs(input - pre_value) < move_limit:
        {
            input = pre_value;
        }

        drop_vect.clear();

        return input;
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



