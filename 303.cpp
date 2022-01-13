// https://leetcode.com/problems/range-sum-query-immutable/submissions/
#include <vector>
using namespace std;

class NumArray {
public:
    vector<int> nums_array;
        
    NumArray(vector<int>& nums) {
        nums_array = nums;
    }
    
    int sumRange(int left, int right) {
        int sum = accumulate(nums_array.begin() + left, nums_array.begin() + right+1, 0);
        return sum;
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */