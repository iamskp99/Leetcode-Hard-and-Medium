func resilientSubarray(nums []int, k int) int {
    pr := []int{}
    som := 0
    i := 0
    n := len(nums)
    for i < n{
        som += nums[i]
        pr = append(pr,som)
        i += 1
    }
    
    i = 0
    ans := 0
    for i < n{
        j := i
        dSom := 0
        if i > 0{
            dSom = pr[i-1]
        }
        s := map[int]int{}
        for j < n{
            curSom := pr[j]-dSom
            cVal := curSom%k
            eVal := nums[j]%k
            s[eVal] = -1
            _,ok := s[cVal]
            if ok{
                if len(s) == 1{
                    ans = max(ans,j-i+1)
                }
            }
            j += 1
        }
        i += 1
    }
    return ans
}