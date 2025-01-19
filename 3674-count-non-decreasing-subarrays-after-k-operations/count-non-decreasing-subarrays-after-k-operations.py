class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        p,s,n,dp,ans = [],[],len(nums),{},0
        prev = 0
        for i in range(n):
            x = nums[i]
            prev += x
            p.append(prev)

        i,stack = n-1,[]
        while i > -1:
            x = nums[i]
            
            while len(stack) > 0:
                if stack[-1][0] < x:
                    stack.pop()
                    continue

                break

            prev_p = p[i-1] if i > 0 else 0
            next_p = p[-1] if len(stack) == 0 else p[stack[-1][1]-1]
            ind = n-1 if len(stack) == 0 else stack[-1][1]-1
            som = 0 if len(stack) == 0 else dp[stack[-1][1]]
            diff,total = next_p-prev_p,(ind-i+1)*x
            res = (total-diff)+som
            stack.append([x,i])
            dp[i] = res
            low,high = 0,len(stack)-1
            cur_k,now_ans = k,-1
            while low <= high:
                mid = (low+high)//2
                sub = 0 if mid == 0 else dp[stack[mid-1][1]]
                if dp[stack[-1][1]]-sub <= cur_k:
                    now_ans = mid
                    high = mid-1

                else:
                    low = mid+1

            if now_ans == 0:
                # if i == 0:
                #     print("dP",dp[0])
                ans += (n-i)

            elif now_ans == -1:
                now_ind = stack[now_ans][1]
                low,high = now_ind,len(nums)-1 if len(stack) == 1 else stack[-2][1]-1
                cur_ans = now_ind

                # if i == 0:
                #     print("JJAJKS",stack,now_ind)

                while low <= high:
                    mid = (low+high)//2
                    # if mid == 1:
                    #     print(diff,sub_total)
                    diff = p[mid]-p[now_ind]
                    sub_total = (mid-now_ind)*stack[now_ans][0]
                    # if mid == 1:
                    #     print(diff,sub_total,"HII")

                    if (sub_total-diff) <= cur_k:
                        low = mid+1
                        cur_ans = mid

                    else:
                        high = mid-1

                # print("KKK",cur_ans)
                if cur_ans > -1:
                    ans += (cur_ans-now_ind+1)


            else:
                # print(i,now_ans,"jjk")
                cur_k -= (dp[stack[-1][1]]-dp[stack[now_ans-1][1]])
                now_ind = stack[now_ans-1][1]
                ans += (now_ind-i)
                now_ans -= 1
                low,high = stack[now_ans][1],len(nums)-1 if now_ans == 0 else stack[now_ans-1][1]-1
                cur_ans = -1
                while low <= high:
                    mid = (low+high)//2
                    diff = p[mid]-p[now_ind]
                    sub_total = (mid-now_ind)*stack[now_ans][0]
                    if (sub_total-diff) <= cur_k:
                        low = mid+1
                        cur_ans = mid

                    else:
                        high = mid-1

                if cur_ans > -1:
                    ans += (cur_ans-now_ind+1)

            # print(i,ans)
            i -= 1

        return ans