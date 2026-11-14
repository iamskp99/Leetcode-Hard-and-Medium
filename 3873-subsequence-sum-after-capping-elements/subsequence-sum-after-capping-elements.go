import (
    "slices"
)

var dp [][]int
var n,ans int

func rec(i,j int,nums *[]int) int{
    if j == 0{  
        return 1
    }
    if i == -1 || j < 0{
        return 0
    }

    if dp[i][j] != -1{
        return dp[i][j]
    }
    cur := rec(i-1,j,nums)
    val := j-((*nums)[i])
    cur = cur|rec(i-1,val,nums)
    
    dp[i][j] = cur
    return cur
}

func subsequenceSumAfterCapping(nums []int, k int) []bool {
    i := 0
    ans = 5000
    n = len(nums)
    dp = nil
    slices.Sort(nums)
    for i < n{
        o := make([]int, k+1)
        for j := range o{
            o[j] = -1
        }
        dp = append(dp,o)
        i += 1
    }
    result := []bool{}
    p := 0
    for x := 1; x <= n; x++ {
        for p < n && nums[p] <= x {
            p += 1
        }
        flag := false
        t := 0
        for t <= n-p {
            now := k-(t*x)
            if now < 0{
                break
            }
            if now == 0 || (p > 0 && rec(p-1, now, &nums) == 1) {
                flag = true
                break
            }
            t += 1
        }
        result = append(result,flag)
    }
    return result
}