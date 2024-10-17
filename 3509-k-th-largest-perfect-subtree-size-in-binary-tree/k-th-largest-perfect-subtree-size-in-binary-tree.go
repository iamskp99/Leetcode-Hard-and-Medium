/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type binar int

func rec(node *TreeNode,ans *[]binar) int{
    if node == nil{
        return 0
    }
    e1 := rec(node.Left,ans)
    e2 := rec(node.Right,ans)
    if e1 != e2{
        return -100000
    }
    if 1+e1+e2 < 0{
        return -100000
    }

    *ans = append(*ans,binar(1+e1+e2))
    return 1+e1+e2
}

func kthLargestPerfectSubtree(root *TreeNode, k int) int {
    var ans[] binar
    rec(root,&ans)
    sort.Slice(ans, func(i, j int) bool { return ans[i] > ans[j] })
    if len(ans) < k{
        return -1
    }
    return int(ans[k-1])
}