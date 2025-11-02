#include <vector>
using namespace std;

class Solution {
public:
    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        vector<vector<int>> grid(m, vector<int>(n, 0)); // Initialize the grid

        // Mark guards and walls on the grid
        for (const auto& guard : guards) {
            grid[guard[0]][guard[1]] = 1;
        }
        for (const auto& wall : walls) {
            grid[wall[0]][wall[1]] = 2;
        }

        // Helper function to mark cells guarded by a guard
        auto mark_guarded = [&](int r, int c) {
            // Mark downwards
            for (int row = r + 1; row < m; ++row) {
                if (grid[row][c] == 1 || grid[row][c] == 2) break;
                grid[row][c] = 3;
            }
            // Mark upwards
            for (int row = r - 1; row >= 0; --row) {
                if (grid[row][c] == 1 || grid[row][c] == 2) break;
                grid[row][c] = 3;
            }
            // Mark rightwards
            for (int col = c + 1; col < n; ++col) {
                if (grid[r][col] == 1 || grid[r][col] == 2) break;
                grid[r][col] = 3;
            }
            // Mark leftwards
            for (int col = c - 1; col >= 0; --col) {
                if (grid[r][col] == 1 || grid[r][col] == 2) break;
                grid[r][col] = 3;
            }
        };

        // Mark all cells guarded by each guard
        for (const auto& guard : guards) {
            mark_guarded(guard[0], guard[1]);
        }

        // Count unguarded cells
        int res = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 0) {
                    ++res;
                }
            }
        }

        return res;
    }
};
