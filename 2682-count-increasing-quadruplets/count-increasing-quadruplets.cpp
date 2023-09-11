class Solution {
public:
    long long countQuadruplets(vector<int>& nums) {
        long long int n = nums.size();
        vector<vector<int>> p(n, vector<int>(n, 0));
        vector<vector<int>> s(n, vector<int>(n, 0));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                p[i][j] = 0;
                s[i][j] = 0;
            }
        }

        for (int i = 0; i < n; i++) {
            int x = nums[i];
            int j = i - 1;
            while (j > -1) {
                if (nums[j] < x) {
                    s[i][j] = 1 + s[i][j + 1];
                } else {
                    s[i][j] = s[i][j + 1];
                }
                j--;
            }

            for (int j = i + 1; j < n; j++) {
                if (nums[j] > x) {
                    p[i][j] = 1 + p[i][j - 1];
                } else {
                    p[i][j] = p[i][j - 1];
                }
            }
        }

        long long ans = 0;
        for (int j = 1; j < n - 1; j++) {
            for (int k = j + 1; k < n; k++) {
                if (nums[j] > nums[k]) {
                    ans += ((s[k][0] - s[k][j]) * (p[j][n - 1] - p[j][k]));
                }
            }
        }

        return ans;
    }
};