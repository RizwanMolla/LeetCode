#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxDistinctElements(vector<int>& nums, int k) {
        // Step 1: Sort the numbers
        sort(nums.begin(), nums.end());
        
        int ans = 0;           // Count of distinct elements
        int pre = INT_MIN;     // Last chosen distinct number
        
        // Step 2: Process each element
        for (int x : nums) {
            // Find the smallest possible value > pre
            // that lies in the range [x - k, x + k]
            int cur = min(x + k, max(x - k, pre + 1));
            
            // If such a value exists (cur > pre), choose it
            if (cur > pre) {
                ans++;
                pre = cur; // Update the last chosen number
            }
        }
        
        return ans;
    }
};