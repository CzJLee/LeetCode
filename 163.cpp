// https://leetcode.com/problems/missing-ranges/submissions/
class Solution {
public:
    vector<string> findMissingRanges(vector<int>& nums, int lower, int upper) {
        vector<string> missing_range;
        if (nums.size() == 0) {
            if (lower == upper) {
                missing_range.push_back(to_string(upper));
            }
            else {
                // Large range
                string range = to_string(lower) + "->" + to_string(upper);
                missing_range.push_back(range);
            }
            return missing_range;
        }
        int previous = lower - 1;
        int n;
        for (int i = 0; i <= nums.size(); i++) {
            if (i == nums.size()) {
                n = upper + 1;
            }
            else {
                n = nums[i];
            }
            
            int diff = n - previous;
            
            if (diff <= 1) {
                // Sequential numbers, nothing to add to the missing range
            } 
            else if (diff == 2) {
                // Only one number gap
                int missing_number = n - 1;
                missing_range.push_back(to_string(missing_number));
            }
            else {
                // Large range
                int missing_lower = previous + 1;
                int missing_upper = n - 1;
                string range = to_string(missing_lower) + "->" + to_string(missing_upper);
                missing_range.push_back(range);
            }
            // Increment previous
            previous = n;
        }
        return missing_range;
    }
};