class Solution {
public:
    int minimumDeviation(vector<int>& nums) {
        multiset<int> m;
        int n = nums.size();
        int i = 0;
        int x,y,z;
        while(i < n){
            x = nums[i];
            if(x%2 == 1){
             m.insert(x*2);   
            }
            else{
                m.insert(x);
            }
            i += 1;
        }
        int ans = 10000000007;
        y = 0;
        while(y == 0){
            auto it1 = m.begin();
            auto it2 = m.end();
            auto it3 = prev(it2);
            x = *it1;
            z = *it3;
            ans = min(ans,z-x);
            if(z%2 == 1){
                y = 1;
                break;
            }
            m.erase(it3);
            m.insert(z/2);
        }
        return ans;
    }
};