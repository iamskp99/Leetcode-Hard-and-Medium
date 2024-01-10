class Solution {
public:
    int dp[100001][15];
    int n,c;
    map<int,vector<int>> d;

    int rec(int i,int p,int parent,vector<int>& coins){
        if(dp[i][p] != -1){
            return dp[i][p];
        }
        int tpow = pow(2,p);
        int val = coins[i]/tpow;
        int cnt1=val/2,cnt2=val-c,ans;
        for(auto x:d[i]){
            if(x != parent){
                cnt1 += rec(x,min(14,p+1),i,coins);
                cnt2 += rec(x,p,i,coins);
            }
        }
        ans = max(cnt1,cnt2);
        dp[i][p] = ans;
        return ans;
    }

    int maximumPoints(vector<vector<int>>& edges, vector<int>& coins, int k) {
        // memset(dp,-1,sizeof(dp));
        int cc,j = 0;
        n = coins.size();
        while(j < n){
            cc = 0;
            while(cc < 15){
                dp[j][cc] = -1;
                cc += 1;
            }
            j += 1;
        }
        c = k;
        int u,v,i = 0;
        while(i < edges.size()){
            u = edges[i][0];
            v = edges[i][1];
            d[u].push_back(v);
            d[v].push_back(u);
            i += 1;
        }
        return rec(0,0,-1,coins);
    }
};