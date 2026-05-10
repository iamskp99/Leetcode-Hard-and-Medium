class Solution {
public:
    vector<int> divisors(int n) {
        vector<int> l;

        for (int i = 1; 1LL * i * i <= n; i++) {
            if (n % i == 0) {
                l.push_back(i);

                if (i != n / i) {
                    l.push_back(n / i);
                }
            }
        }

        return l;
    }
    
    long long minArraySum(vector<int>& nums) {
        ios::sync_with_stdio(false);
        cin.tie(nullptr);

        unordered_set<int> s(nums.begin(), nums.end());

        sort(nums.begin(), nums.end());

        long long ans = 0;

        for (int x : nums) {
            vector<int> d = divisors(x);

            sort(d.begin(), d.end());

            bool found = false;

            for (int ele : d) {
                if (ele != x && s.count(ele)) {
                    ans += ele;
                    found = true;
                    break;
                }
            }

            if (!found) {
                ans += x;
            }
        }

        return ans;
    }
};