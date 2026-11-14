import (
    "slices"
)

func calculateSum(a,x int64) int64{
    som := ((x)*((2*a)+x-1))/2
    return int64(som)
}

func minimalKSum(nums []int, k int) int64 {
    slices.Sort(nums)
    i,n := 0,len(nums)
    var ans,cnt,ck int64
    ans = 0
    cnt = 0
    ck = int64(k)
    // fmt.Println(nums)
    nums = slices.Insert(nums, 0, 0)
    n = n+1
    for i < n && cnt < ck{
        if i == n-1{
            // ans += int64(nums[i])
            if cnt < ck{
                ans += calculateSum(int64(nums[i]+1),int64(k)-cnt)
                cnt = ck
            }
        }else{
            // ans += int64(nums[i])
            if nums[i] == nums[i+1]{
                
            }else{
                ee := min(int64(k)-cnt,int64(nums[i+1]-nums[i]-1))
                // fmt.Println("LL",int64(k)-cnt,int64(nums[i+1]-nums[i]-2))
                diff := int64(ee)
                if diff >= 1 && cnt < ck{
                    // fmt.Println(i,diff)
                    ans += calculateSum(int64(nums[i]+1),int64(diff))
                    cnt += diff
                }
            }
        }
        i += 1
    }
    return ans
}