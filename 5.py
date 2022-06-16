import math
class Solution: 
    def longestPalindrome(self, s: str) -> str:
        # Move along s, and check sides.
        # If pal, keep moving, else move to next index
        longest_pal = ""

        for i in range(len(s) * 2):
            len_longest_pal = len(longest_pal)
            left_index = math.floor(i / 2) - len_longest_pal // 2
            right_index = math.ceil(i / 2) + len_longest_pal // 2
            test_str = s[left_index : right_index + 1]
            if self.isPal(test_str):
                while test_str[0] == test_str[-1]:
                    if len(test_str) > len(longest_pal):
                        longest_pal = test_str
                    
                    # Check next
                    left_index -= 1
                    right_index += 1
                    if left_index >= 0 and right_index < len(s):
                        test_str = s[left_index : right_index + 1]
                    else:
                        break
        
        return longest_pal

    def isPal(self, s):
        max_index = len(s) - 1
        for i in range(len(s)):
            if s[i] != s[max_index - i]:
                return False
        
        return True

    # Longest_Palindrome(string S) {
    #     string S' = S with a bogus character (eg. '|') inserted between each character (including outer boundaries)
    #     array PalindromeRadii = [0,...,0] // The radius of the longest palindrome centered on each place in S'
    #     // note: length(S') = length(PalindromeRadii) = 2 × length(S) + 1
        
    #     Center = 0
    #     Radius = 0
        
    #     while Center < length(S') {
    #         // At the start of the loop, Radius is already set to a lower-bound for the longest radius.
    #         // In the first iteration, Radius is 0, but it can be higher.
            
    #         // Determine the longest palindrome starting at Center-Radius and going to Center+Radius
    #         while Center-(Radius+1) >= 0 and Center+(Radius+1) < length(S') and S'[Center-(Radius+1)] = S'[Center+(Radius+1)] {
    #             Radius = Radius+1
    #         }             
         
    #         // Save the radius of the longest palindrome in the array
    #         PalindromeRadii[Center] = Radius
            
    #         // Below, Center is incremented.
    #         // If any precomputed values can be reused, they are.
    #         // Also, Radius may be set to a value greater than 0
            
    #         OldCenter = Center
    #         OldRadius = Radius
    #         Center = Center+1
    #         // Radius' default value will be 0, if we reach the end of the following loop. 
    #         Radius = 0 
    #         while Center <= OldCenter + OldRadius {
    #             // Because Center lies inside the old palindrome and every character inside
    #             // a palindrome has a "mirrored" character reflected across its center, we
    #             // can use the data that was precomputed for the Center's mirrored point. 
    #             MirroredCenter = OldCenter - (Center - OldCenter)
    #             MaxMirroredRadius = OldCenter + OldRadius - Center
    #             if PalindromeRadii[MirroredCenter] < MaxMirroredRadius {
    #                 PalindromeRadii[Center] = PalindromeRadii[MirroredCenter]
    #                 Center = Center+1
    #             }   
    #             else if PalindromeRadii[MirroredCenter] > MaxMirroredRadius {
    #                 PalindromeRadii[Center] = MaxMirroredRadius
    #                 Center = Center+1
    #             }   
    #             else { // PalindromeRadii[MirroredCenter] = MaxMirroredRadius
    #                 Radius = MaxMirroredRadius
    #                 break  // exit while loop early
    #             }   
    #         }      
    #     }
        
    #     longest_palindrome_in_S' = 2*max(PalindromeRadii)+1
    #     longest_palindrome_in_S = (longest_palindrome_in_S'-1)/2
    #     return longest_palindrome_in_S 
    # }

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Manacher's algorithm
        s_expanded = []
        for char in s:
            s_expanded.append(char)
            s_expanded.append("|")
        s_expanded.pop()

        longest_radius = [0 for _ in range(len(s_expanded))]

        center = 0
        radius = 0

        while center < len(s_expanded):
            # Determine the longest palindrome starting at (center - radius) and going to (center + radius)
            while (center - radius - 1) >= 0 and (center + radius + 1) < len(s_expanded) and s_expanded[center - radius - 1] == s_expanded[center + radius + 1]:
                radius += 1
            
            # Save the radius of the longest palindrome in the array
            longest_radius[center] = radius

            # If any precomputed values can be reused, they are. 

            old_center = center
            old_radius = radius 
            center += 1
            radius = 0

            while center <= old_center + old_radius:
                # Because center lies inside the old palindrome and every character inside a palindrome has a "mirrored" character reflected across its center,
                # We can use the data that was precomputed for the center's mirrored point
                mirrored_center = old_center - (center - old_center)
                max_mirrored_radius = old_center + old_radius - center
                if longest_radius[mirrored_center] < max_mirrored_radius:
                    longest_radius[center] = longest_radius[mirrored_center]
                    center += 1
                elif longest_radius[mirrored_center] > max_mirrored_radius:
                    longest_radius[center] = max_mirrored_radius
                    center += 1
                else:
                    radius = max_mirrored_radius
                    break

        index_of_center = longest_radius.index(max(longest_radius))
        pal_extended = s_expanded[index_of_center-longest_radius[index_of_center]:index_of_center + longest_radius[index_of_center] + 1]

        longest_palindrome_in_s_extended = 2 * max(longest_radius) + 1
        longest_palindrome_in_s = (longest_palindrome_in_s_extended - 1) / 2
        longest_pal = "".join(char for char in pal_extended if char != "|")
        return longest_pal

class Solution:
    #Manacher algorithm
    #http://en.wikipedia.org/wiki/Longest_palindromic_substring
    
    def longestPalindrome(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
    
            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]
    
        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]