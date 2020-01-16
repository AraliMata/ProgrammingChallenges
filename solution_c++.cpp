#include <sstream>
#include <string>
using namespace std;

class Solution {
public:
    int subtractProductAndSum(int n) {
        string number = "";
        string digit = "";
        int len = 0;
        int product = 1;
        int summ = 0;
        int digitInt = 0;
        int diff;

        stringstream ss;
        ss << n;
        ss >> number;

        for (int i = 0; i <  number.length(); i++){
            digit = number[i];

            stringstream s;
            s << digit;
            s >> digitInt;

            product *= digitInt;
            summ += digitInt;
        }

        diff = product - summ;

    return diff;

    }
};
