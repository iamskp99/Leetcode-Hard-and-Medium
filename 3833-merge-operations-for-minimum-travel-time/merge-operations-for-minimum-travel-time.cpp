class Solution {
public:
    int recursion(int pos, int currK, int currTime, int n, int k, vector<int> &position, vector<int> &time, vector<vector<vector<int>>> &dp) {
        if(pos == n - 1) {
            return (currK > 0 ? INT_MAX : 0);
        }
        
        if(dp[pos][currK][currTime] != -1) {
            return dp[pos][currK][currTime];
        }
        
        int ans = INT_MAX;
        
        int res = recursion(pos + 1, currK, time[pos + 1], n, k, position, time, dp);        
        if(res != INT_MAX) {
            ans = min(ans, (position[pos + 1] - position[pos]) * currTime + res);
        }
        
        if(currK > 0) {
            int timeSum = time[pos + 1], operations = 0;
            for(int nextIdx = pos + 2; nextIdx <= min(n - 1, pos + currK + 1); nextIdx++) {
                timeSum += time[nextIdx], operations++;
                
                int res = recursion(nextIdx, currK - operations, timeSum, n, k, position, time, dp);
                if(res != INT_MAX) {
                    ans = min(ans, (position[nextIdx] - position[pos]) * currTime + res);
                }
            }
        }
        
        return dp[pos][currK][currTime] = ans;
    }
    
    int minTravelTime(int l, int n, int k, vector<int> &position, vector<int> &time) {
        int sum = 0;
        for(auto &x: time) sum += x;
        
        vector<vector<vector<int>>> dp(n, vector<vector<int>> (k + 1, vector<int> (sum + 1, -1)));
        return recursion(0, k, time[0], n, k, position, time, dp);
    }
};