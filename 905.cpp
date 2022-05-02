// https://leetcode.com/problems/sort-array-by-parity/

class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& nums) {
        vector<int> evens;
        vector<int> odds;
        
        for (auto num: nums) {
            if (num % 2 == 0) {
                evens.push_back(num);
            }
            else {
                odds.push_back(num);
            }
        }
        
        vector<int> together;
        together.reserve( evens.size() + odds.size() ); // preallocate memory
        together.insert( together.end(), evens.begin(), evens.end() );
        together.insert( together.end(), odds.begin(), odds.end() );

        return together;
    }
};