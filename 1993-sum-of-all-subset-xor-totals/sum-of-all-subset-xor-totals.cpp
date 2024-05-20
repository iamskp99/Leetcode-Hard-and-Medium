class Solution {
public:
    vector <vector <int>> dp;
    int func(vector <int>& nums,int i,int x)
    {
        if(i==nums.size())
        {
            return x;
        }
        if(dp[i][x]!=-1) return dp[i][x];
        return dp[i][x] = func(nums,i+1,x^nums[i]) + func(nums,i+1,x);
    }
    int subsetXORSum(vector<int>& nums)
    {
        dp.resize(nums.size(),vector <int> (10000,-1));
        return func(nums,0,0);
    }
};