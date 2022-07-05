class Solution {
public:
    long long dp[1001][1001];
    long long M,n,m;
    long long ans;
    long long helper(long long i,long long j,vector<vector<int>>& grid){
        if(dp[i][j] != -1){
            return dp[i][j];
        }
        long long cnt = 1;
        vector<pair<int,int>> edges;
        edges.push_back({i-1,j});
        edges.push_back({i,j+1});
        edges.push_back({i+1,j});
        edges.push_back({i,j-1});
        int ei,i1,j1;
        ei = 0;
        while(ei < 4){
            i1 = edges[ei].first;
            j1 = edges[ei].second;
            if((i1 >= 0)&&(i1 < n)&&(j1 >= 0)&&(j1 < m)){
                if(grid[i1][j1] > grid[i][j]){
                    cnt = (cnt+helper(i1,j1,grid))%M;
                }
            }
            ei += 1;
        }
        ans = (ans+cnt)%M;
        dp[i][j] = cnt;
        return cnt;
    }
    
    int countPaths(vector<vector<int>>& grid) {
        long long i,j,som;
        M = 1000000007;
        n = grid.size();
        m = grid[0].size();
        i = 0;
        while(i < n){
            j = 0;
            while(j < m){
                dp[i][j] = -1;
                j += 1;
            }
            i += 1;
        }
        ans = 0;
        // Helper Function Call
        i = 0;
        while(i < n){
            j = 0;
            while(j < m){
                if(dp[i][j] == -1){
                    som = helper(i,j,grid);
                }
                j += 1;
            }
            i += 1;
        }
        return ans;
    }
};