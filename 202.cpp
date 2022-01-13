class Solution {
public:
    bool isHappy(int n) {
        unordered_set <int> seen;
        
        while (n != 1) {
            n = digitSumSquares(n);
            // Check if n has been seen
            if (seen.count(n)) {
                return false;
            }
            seen.insert(n);
        }
        
        return true;
    }
    
    int digitSumSquares(int n) {
        int sum_squares = 0;
        while (n > 0) {
            div_t divmod = div(n, 10);
            n = divmod.quot;
            int mod = divmod.rem;
            sum_squares += pow(mod, 2);
        }
        return sum_squares;
    }
};