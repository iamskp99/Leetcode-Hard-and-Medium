class Solution {
public:
    long long dp[201][201];
    map<pair<long long,long long>,long> mp; 
    long long helper1(int i,int j){
        long long ans = 0;
        long long e1,e2;
        if(dp[i][j] != -1){
            return dp[i][j];
        }
        if(mp.find({i,j}) != mp.end()){
            ans = mp[{i,j}];
        }
        e1 = 1;
        while(e1 <= i/2){
            ans = max(ans,helper1(e1,j)+helper1(i-e1,j));
            e1 += 1;
        }
        e2 = 1;
        while(e2 <= j/2){
              ans = max(ans,helper1(i,j-e2)+helper1(i,e2));
              e2 += 1;
        }
        dp[i][j] = ans;
        return dp[i][j];
    }
    
    long long sellingWood(int m, int n, vector<vector<int>>& prices) {
        long long i,j,u,v,w;
        i = 0;
        while(i < prices.size()){
            u = prices[i][0];
            v = prices[i][1];
            w = prices[i][2];
            mp[{u,v}] = w;
            i += 1;
        }
        i = 0;
        while(i < 201){
            j = 0;
            while(j < 201){
                dp[i][j] = -1;
                j += 1;
            }
            i += 1;
        }
        return helper1(m,n);
    }
};