// https://leetcode.com/problems/valid-palindrome/submissions/
class Solution {
public:
    bool isPalindrome(string s) {
        size_t i = 0;
        size_t len = s.length();
        while(i < len){
            if (!isalnum(s[i]) || s[i] == ' '){
                s.erase(i,1);
                len--;
            }else
                i++;
        }
        transform(s.begin(), s.end(), s.begin(), ::tolower);
        string s_reverse = s;
        reverse(s_reverse.begin(), s_reverse.end());
        return s == s_reverse;
    }
};