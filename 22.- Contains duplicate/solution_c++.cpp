#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> nums1(nums.begin(), nums.end());
        
        if(nums1.size() == nums.size()){
            return false;
        }else{
            return true;
        }
        
        return false;
    }
};