#include <String>
using namespace std;
class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int jewelNum = 0;
        int lenJ = J.length();
        int lenS = S.length();

        for(int i = 0; i < lenJ; i++){
            for(int j = 0; j < lenS; j++){

                if(J[i] == S[j]){
                    jewelNum ++;
                }

            }
        }

    return jewelNum;
    }
};
