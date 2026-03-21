class Solution {
public:
    int dp[300][5001];
    int n;
    int rec(int i,int amount,vector<int>& coins){
        if(amount < 0){
            return 0;
        }

        if(i == n){
            if(amount == 0){
                return 1;
            }
            return 0;
        }

        if (dp[i][amount] != -1){
            return dp[i][amount];
        }

        int ans = rec(i,amount-coins[i],coins)+rec(i+1,amount,coins);
        return dp[i][amount] = ans;
    }

    int change(int amount, vector<int>& coins) {
        n = coins.size();
        memset(dp,-1,sizeof(dp));
        return rec(0,amount,coins);
    }
};