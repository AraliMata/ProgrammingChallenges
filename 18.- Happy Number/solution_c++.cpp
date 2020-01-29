#include <cmath>
#include <set>

using namespace std;

class Solution {
public:
    bool isHappy(int n) {
        int i = 0;
        set<int> numbers;
        
        while(i != 0) {
            i = 0;
            
            while(n > 0) {
                i += pow(n % 10, 2);
                n = n / 10;
            }
            
            if(i == 0) {
                return true;
            }else if(numbers.count(i)){
                return false; 
            }else{
                n = i;
                numbers.insert(i);
            }
            
        }
        
        return true;
    }
};