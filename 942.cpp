// https://leetcode.com/problems/di-string-match/submissions/
class Solution {
public:
    vector<int> diStringMatch(string s) {
        vector<int> perm;
        int high = s.length();
        int low = 0;
        
        for (char letter : s) {
            if (letter == 'I') {
                perm.push_back(low);
                low++;
            }
            else if (letter == 'D') {
                perm.push_back(high);
                high--;
            }
        }
        perm.push_back(high);
        return perm;
    }
};