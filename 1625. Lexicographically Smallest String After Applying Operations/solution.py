#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    string findLexSmallestString(string s, int a, int b) {
        queue<string> q;               // For BFS traversal
        unordered_set<string> vis;     // To track visited strings
        q.push(s);
        vis.insert(s);
        string ans = s;                // Initialize smallest string
        int n = s.size();

        while (!q.empty()) {
            s = q.front();
            q.pop();

            // Update smallest lexicographically
            ans = min(ans, s);

            // Operation 1: Add 'a' to digits at odd indices
            string t1 = s;
            for (int i = 1; i < n; i += 2) {
                t1[i] = (t1[i] - '0' + a) % 10 + '0';
            }

            // Operation 2: Rotate right by b positions
            string t2 = s.substr(n - b) + s.substr(0, n - b);

            // Enqueue both if not visited before
            if (!vis.count(t1)) {
                vis.insert(t1);
                q.push(t1);
            }
            if (!vis.count(t2)) {
                vis.insert(t2);
                q.push(t2);
            }
        }
        return ans;
    }
};