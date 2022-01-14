// https://leetcode.com/problems/plus-one/submissions/
class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int i = digits.size() - 1;
        int carry = 1;
        while (i >= 0) {
            digits[i] += carry;
            carry = 0;
            if (digits[i] == 10) {
                digits[i] = 0;
                carry = 1;
            }
            i--;
        }
        if (carry == 1) {
            digits.insert(digits.begin(), carry);
        }
        return digits;
    }
};