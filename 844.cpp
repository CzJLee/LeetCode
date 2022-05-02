// https://leetcode.com/problems/backspace-string-compare/

class Solution {
public:
    string typed(string s) {
        vector<char> s_list = {};
        for (char c: s) {
            if (c == '#') {
                if (s_list.size() > 0) {
                    s_list.pop_back();
                } 
            }
            else {
                s_list.push_back(c);
            }
        }
        string s_typed(s_list.begin(), s_list.end());
        return s_typed;
    }
    bool backspaceCompare(string s, string t) {
        return typed(s) == typed(t);
    }
};