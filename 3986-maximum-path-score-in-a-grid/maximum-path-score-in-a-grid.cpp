int dp[200][200][1001];
class Solution {
public:
    int n,m;

    int rec(int i,int j,int k,vector<vector<int>>& grid){
        if((i == -1)||(i == n)||(j == -1)||(j == m)){
            return -1;
        }

        if(dp[i][j][k] != -10){
            return dp[i][j][k];
        }

        int cost = k;
        int value = grid[i][j];
        if(value != 0){
            cost -= 1;
        }

        if(cost < 0){
            return dp[i][j][k] = -1;
        }

        if((i == n-1)&&(j == m-1)){
            return dp[i][j][k] = value;
        }

        int ans = -1;
        if(rec(i+1,j,cost,grid) != -1){
            ans = max(ans,value+rec(i+1,j,cost,grid));
        }

        if(rec(i,j+1,cost,grid) != -1){
            ans = max(ans,value+rec(i,j+1,cost,grid));
        }

        return dp[i][j][k] = ans;
    }


    int maxPathScore(vector<vector<int>>& grid, int k) {
        n = grid.size();
        m = grid[0].size();
        int i,j,l;
        i = 0;
        while(i < n){
            j = 0;
            while(j < m){
                l = 0;
                while(l < k+1){
                    dp[i][j][l] = -10;
                    l += 1;
                }
                j += 1;
            }
            i += 1;
        }
        // memset(dp,-1,sizeof(dp));
        return rec(0,0,k,grid);
    }
};