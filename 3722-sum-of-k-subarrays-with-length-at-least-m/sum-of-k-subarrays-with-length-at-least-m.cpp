class Solution {
public:
    int dp[2001][2001][4];
    int n;

    int rec(int i,int ck,int cm,vector<int>& nums,int k,int m){
        if(ck > k){
            return -100000000;
        }

        if(i == n){
            if(ck < k){
                return -100000000;
            }
            if((cm == m) || (cm == 0)){
                return 0;
            }
            return -100000000;
        }

        if(dp[i][ck][cm] != 100000000){
            return dp[i][ck][cm];
        }

        
        int ans = -100000000; 
        if(cm == m){
            ans = max(ans,nums[i]+rec(i+1,ck,cm,nums,k,m));
            ans = max(ans,rec(i,ck,0,nums,k,m));
        }else{
            if(cm == 0){
                ans = max(ans,rec(i+1,ck,cm,nums,k,m));
                ans = max(ans,nums[i]+rec(i+1,ck+1,1,nums,k,m));
            }else{
                ans = max(ans,nums[i]+rec(i+1,ck,cm+1,nums,k,m));
            }
        }
        return dp[i][ck][cm] = ans;
    }

    int maxSum(vector<int>& nums, int k, int m) {
        n = nums.size();
        int a,b,c,con;
        a = 0;
        while(a <= n){
            b = 0;
            while(b <= k){
                c = 0;
                while(c <= m){
                    dp[a][b][c] = 100000000;
                    c += 1;
                }
                b += 1;
            }
            a += 1;
        }
        return rec(0,0,0,nums,k,m);
    }
};