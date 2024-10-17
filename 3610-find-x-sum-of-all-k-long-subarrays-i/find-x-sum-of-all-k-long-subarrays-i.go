func findXSum(nums []int, k int, x int) []int {
    var ans[] int
    var temp[] int
    type com struct{
        num int
        val int
    }

    var er[] com
    var i = 0
    for i = 0; i < len(nums) ; i++{
        temp = []int {}
        er = []com {}
        d := make(map[int]int)

        for j := i; j < min(len(nums),i+k); j++{
            temp = append(temp,nums[j])
            d[nums[j]] += 1
        }

        if len(temp) < k{
            break
        }
        // fmt.Println(temp)

        for key, value := range d {
            e := com{num:key,val:value}
            er = append(er,e)
        }

        sort.Slice(er, func(i, j int) bool {
            if er[i].val == er[j].val{
                return er[i].num > er[j].num
            }
            return er[i].val > er[j].val
        })

        prev := -1
        som := 0
        uu := 0
        for _, val := range er{
            if val.num == prev || uu >= x{
                continue
            }
            som += val.num*d[val.num]
            prev = val.num
            uu += 1
        }
        ans = append(ans,som)
    }

    return ans

}