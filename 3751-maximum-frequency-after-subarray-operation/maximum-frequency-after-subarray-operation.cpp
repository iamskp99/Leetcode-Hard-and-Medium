class Solution {
public:
    int dp[100000][51][3];
    int n;

    int rec(int i,int j,int c,int k,vector<int>& nums){
        if(i == n){
            return 0;
        }

        if(dp[i][j][c] != -1){
            return dp[i][j][c];
        }
        int ans = 0;
        if(c == 1){
            if(nums[i] == j){
                ans = max(ans,1+rec(i+1,j,c,k,nums));
                ans = max(ans,1+rec(i+1,j,2,k,nums));
            }else{
                ans = max(ans,rec(i+1,j,2,k,nums));
                ans = max(ans,rec(i+1,j,c,k,nums));
            }
        }else{
            if(c == 0){
                if(nums[i] == k){
                    ans = max(ans,1+rec(i+1,j,c,k,nums));
                }else{
                    ans = max(ans,rec(i+1,j,c,k,nums));
                }
                ans = max(ans,rec(i,nums[i],1,k,nums));
            }else{
                if(nums[i] == k){
                    ans = max(ans,1+rec(i+1,j,c,k,nums));
                }else{
                    ans = max(ans,rec(i+1,j,c,k,nums));
                }
            }
        }
        return dp[i][j][c] = ans;
    }

    int maxFrequency(vector<int>& nums, int k) {
        n = nums.size();
        int a,b,c;
        a = 0;
        while(a < n){
            b = 0;
            while(b < 51){
                c = 0;
                while(c < 3){
                    dp[a][b][c] = -1;
                    c += 1;
                }
                b += 1;
            }
            a += 1;
        }
        return rec(0,0,0,k,nums);
    }
};