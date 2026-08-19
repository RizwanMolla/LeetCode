class Solution {
public:
    bool canConstruct(string s, int k) {
        if (s.length() < k) 
            return false;

        vector<int> freq(26, 0);
        for (char c : s) {
            freq[c - 'a']++;
        }

        int oddCount = 0;
        for (int count : freq) {
            if (count % 2 != 0) 
                oddCount++;
        }

        return oddCount <= k;
    }
};
