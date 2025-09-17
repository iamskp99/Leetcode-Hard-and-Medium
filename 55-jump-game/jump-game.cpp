class Solution {
public:
    int dp[10001];
    int n;

    int rec(int i,vector<int>& nums){
        if(i >= n){
            return 0;
        }

        if(i == n-1){
            return 1;
        }

        if(dp[i] != -1){
            return dp[i];
        }
        int ans = 0;
        int ind = i+1;
        int limit = i+nums[i];
        while(ind <= min(limit,n-1)){
            ans = ans|rec(ind,nums);
            ind += 1;
        }
        return dp[i] = ans;
    }


    bool canJump(vector<int>& nums) {
        int i = 0;
        n = nums.size();
        while(i < n){
            dp[i] = -1;
            i += 1;
        }

        if(rec(0,nums) == 1){
            return true;
        }
        return false;
    }
};