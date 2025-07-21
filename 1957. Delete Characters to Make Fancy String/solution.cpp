#include <string>
using namespace std;

class Solution {
public:
    string makeFancyString(string s) {
        string result;
        for (char c : s) {
            int n = result.size();
           
            if (n < 2 || !(result[n - 1] == c && result[n - 2] == c)) {
                result.push_back(c);
            }
        }
        return result;
    }
};