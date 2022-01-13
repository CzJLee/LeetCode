// https://leetcode.com/problems/move-zeroes/submissions/
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int num_len = nums.size();
        for (int i = 0; i < num_len; i++) {
            if (nums[i] == 0) {
                nums.erase(nums.begin() + i);
                nums.push_back(0);
                num_len--;
                i--;
            }
        }
    }
};