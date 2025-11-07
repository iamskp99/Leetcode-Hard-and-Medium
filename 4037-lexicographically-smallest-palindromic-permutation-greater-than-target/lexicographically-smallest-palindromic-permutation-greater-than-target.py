class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        ch = [0 for i in range(26)]
        for i in s:
            e = ord(i)-97
            ch[e] += 1

        n = len(s)
        cur = ["0" for i in range(n)]
        is_flag = True if n%2 else False
        ans = []
        i,j = 0,n-1
        while i < n//2 and j > i:
            # Case 1 : Can we make a palindrome by utilising remaining chars , we will
            # just increase the character of the index , if it is not possible then we will break.
            nch = ch.copy()
            cur_copy = cur.copy()
            tvalue = ord(target[i])-97
            for e in range(tvalue+1,26):
                if nch[e] > 1:
                    cur_copy[i],cur_copy[j] = chr(97+e),chr(97+e)
                    nch[e] -= 2
                    break

            if cur_copy[i] == "0":
                if ch[tvalue] < 2:
                    break

                cur[i],cur[j] = target[i],target[i]
                ch[tvalue] -= 2
                i += 1
                j -= 1
                continue

            is_completed = True
            ci,cj = i+1,j-1
            while ci < n//2:
                for e in range(26):
                    if nch[e] > 1:
                        cur_copy[ci],cur_copy[cj] = chr(97+e),chr(97+e)
                        nch[e] -= 2
                        break

                if cur_copy[ci] == "0":
                    is_completed = False
                    break
                    
                ci += 1
                cj -= 1

            if not is_completed:
                if ch[tvalue] < 2:
                    break

                cur[i],cur[j] = target[i],target[i]
                ch[tvalue] -= 2
                i += 1
                j -= 1
                continue

            if is_flag:
                for e in range(26):
                    if nch[e] == 1:
                        nch[e] -= 1
                        cur_copy[n//2] = chr(97+e)
                        break

            if cur_copy[n//2] == "0":
                if ch[tvalue] < 2:
                    break

                cur[i],cur[j] = target[i],target[i]
                ch[tvalue] -= 2
                i += 1
                j -= 1
                continue
            else:
                ss = "".join(cur_copy)
                # print(ss)
                if ss <= target:
                    pass
                else:
                    ans = cur_copy

            # Case 2 : Carry on with the target value at the current index.
            if ch[tvalue] < 2:
                break

            cur[i],cur[j] = target[i],target[i]
            ch[tvalue] -= 2
            
            j -= 1
            i += 1

        if is_flag:
            for e in range(26):
                if ch[e] == 1:
                    ch[e] -= 1
                    cur[n//2] = chr(97+e)
                    break

        ss = "".join(cur)        
        if ss <= target:
            pass
        else:
            ans = cur

        return "".join(ans) 
        