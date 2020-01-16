#include <string>
using namespace std;
class Solution {
public:
    string defangIPaddr(string address) {
        string new_address = "";

        for(int i = 0; i < address.length(); i++){

            if(address.substr(i,1).compare(".") == 0){
                new_address += "[.]";
            }else{
                new_address += address[i];
            }

        }

        return new_address;
    }
};
