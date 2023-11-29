class Solution {
public:
    #define ll long long
    
    bool isVowel(char ch) {
        return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
    }
    
    ll beautifulSubstrings(std::string s, int k) {
        ll vowel = 0, cons = 0, result = 0;
        unordered_map<ll, unordered_map<ll, ll>> mp;
        mp[0][0] = 1;
        

        for (char ch: s) {
            
            if(isVowel(ch)) {
                vowel++;
            } else {
                cons++;
            }
            
      
            ll pSum = vowel - cons;
            for (auto& [z, count]: mp[pSum]) {
                if ((vowel%k - z) * (vowel%k - z) % k == 0) 
                    result += count;
            }

            ++mp[vowel - cons][vowel%k];

        }
        
        return result;
    }
};