import (
    "sort"
)

type Pair struct{a,b int}

func gcd(x int,y int) int{
    if(y == 0){
        return x
    }
    return gcd(y,x%y)
}

func minimumLines(stockPrices [][]int) int {
    i,n := 0,len(stockPrices)
    // d := map[Pair]int{}
    sort.Slice(stockPrices, func(i,j int) bool{
        if stockPrices[i][0] == stockPrices[j][0]{
            return stockPrices[i][1] < stockPrices[j][1]
        }
        return stockPrices[i][0] < stockPrices[j][0]
    })
    // fmt.Println(stockPrices)
    ans := 0
    px,py := -1,-1
    gx,gy := -1,-1
    for i < n{
        x := min(stockPrices[i][0],stockPrices[i][1])
        y := max(stockPrices[i][0],stockPrices[i][1])
        if(px == -1 && py == -1){
            px,py = x,y
            i += 1
            continue
        }
        vx,vy := x-px,y-py
        curGcd := gcd(vx,vy)
        if curGcd == 0{

        }else{
            vx = vx/curGcd
            vy = vy/curGcd
        }
        if(vx == gx && vy == gy){
            
        }else{
            gx = vx
            gy = vy
            ans += 1
        }
        px,py = x,y
        i += 1
    }
    // fmt.Println(d)
    return ans
}


