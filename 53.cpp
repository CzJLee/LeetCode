#include <vector>
using namespace std;
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector<int> maxSum(nums);

        for (int n = 1; n < size(nums); n++) {
            maxSum[n] = max(maxSum[n], maxSum[n-1] + maxSum[n]);
        }

        return *max_element(maxSum.begin(), maxSum.end());
    }
};