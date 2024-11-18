class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> ans;
        int prev_i= INT_MAX, prev_j = INT_MAX, prev_k = INT_MAX;
        sort(nums.begin(), nums.end());
        for(int i = 0; i< nums.size()-2; ++i){
            if(nums[i] == prev_i){
                continue;
            }
            prev_i = nums[i];
            int j = i+1, k = nums.size()-1;
            prev_j = INT_MAX; 
            prev_k = INT_MAX;
            while( j < k ){
                if(prev_j == nums[j]){
                    ++j;  
                }
                else if(prev_k == nums[k]){
                    --k;
                }
                else if(nums[i] + nums[j] + nums[k] == 0){
                    // break;
                    prev_j = nums[j];
                    prev_k = nums[k];
                    ans.push_back(vector<int>{nums[i], nums[j], nums[k]});
                    ++j;
                    --k;
                }else if( nums[i] + nums[j] + nums[k] < 0){
                    prev_j = nums[j];
                    ++j;
                }else{
                    prev_k = nums[k];
                    --k;
                }
            }    
        }
        return ans;
    }
};