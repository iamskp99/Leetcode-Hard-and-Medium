#define tostr(x) to_string(x)

class Solution {
public:
    long long dp[20][2];
    long long n;
    long long lim;
    string fin,star;

    long long rec(long long i,long long flag,string &st,string &s){
        if(i == n){
            return 1;
        }

        if(dp[i][flag] != -1){
            return dp[i][flag];
        }
        long long ans = 0;
        long long cur = lim;
        long long ee = 9;
        if(flag == 1){
            ee = st[i]-'0';
            cur = min(cur,ee);
        }else{
            cur = min(cur,ee);
        }
        long long now = st.size()-i;
        if(now <= s.size()){
            long long sind = s.size()-now;
            long long snum = s[sind]-'0';
            
            if(flag == 1){
                if(snum > ee){
                    ans = 0;
                }else{
                    if(snum == ee){
                        ans = rec(i+1,1,st,s);
                    }else{
                        ans = rec(i+1,0,st,s);
                        }
                    }
            }else{
                ans = rec(i+1,0,st,s);
            }
            dp[i][flag] = ans;
            return ans;
        }
        long long num = 0;
        while(num <= cur){
            if(num == ee){
                ans = ans+rec(i+1,flag&1,st,s);
            }else{
                long long yy = rec(i+1,0,st,s);
                ans = ans+yy;
            }
            num += 1;
        }
        dp[i][flag] = ans;
        return ans;
    }


    long long numberOfPowerfulInt(long long start, long long finish, int limit, string s) {
        star = tostr(start-1);
        fin = tostr(finish);
        lim = limit;
        memset(dp,-1,sizeof(dp));
        n = fin.size();
        long long ans2;
        if(n < s.size()){
            ans2 = 0;
        }else{
            ans2 = rec(0,1,fin,s);
        }

        memset(dp,-1,sizeof(dp));
        n = star.size();
        long long ans1;
        if(n < s.size()){
            ans1 = 0;
        }else{
            ans1 = rec(0,1,star,s);
        }
        // cout<<ans1<<" as "<<ans2<<"as\n";
        return ans2-ans1;
    }
};