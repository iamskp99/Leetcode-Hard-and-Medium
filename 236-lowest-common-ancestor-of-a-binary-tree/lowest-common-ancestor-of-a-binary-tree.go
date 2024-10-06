/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func rec(node, p , q *TreeNode) *TreeNode{
    if node == nil{
        return nil
    }
    cnt := 0
    if node == p || node == q{
        return node
    }
    q1 := rec(node.Left,p,q)
    q2 := rec(node.Right,p,q)
    var val *TreeNode = nil
    if q1 == p || q1 == q{
        cnt += 1
        val = q1
    }
    if q2 == p || q2 == q{
        cnt += 1
        val = q2
    }

    if cnt == 2{
        return node
    }
    if cnt == 0{
        if q1 != nil{
            return q1
        }

        if q2 != nil{
            return q2
        }

        return nil
    }

    return val
}


 func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
    return rec(root,p,q)
}