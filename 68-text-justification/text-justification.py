class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []
        words = words[::-1]
        while len(words) > 0:
            l = []
            cnt,size = 0,0
            while len(words) > 0 and size+len(words[-1]) <= maxWidth:
                w = words.pop()
                l.append(w)
                l.append(" ")
                size += (len(w)+1)
                cnt += 1

            size -= 1
            l.pop()
            rem = maxWidth-size
            divCnt = cnt-1 if cnt > 1 else 1
            even = rem//divCnt
            mod = rem%divCnt
            # flag = 1
            nowL = []
            if len(words) == 0:
                l.append(" "*rem)
                nowL = l

            elif cnt == 1:
                nowL.append(l.pop())
                nowL.append(" "*even)

            else:
                i,ind = 0,0
                while i < cnt:
                    ele = l[ind]
                    if i == cnt-1:
                        nowL.append(ele)
                    else:
                        nowL.append(ele)
                        ind += 1
                        nowL.append(l[ind])
                        if mod > 0:
                            nowL.append(" "*even)
                            nowL.append(" ")
                            mod -= 1
                            # flag = 0
                        else:
                            nowL.append(" "*even)

                    i += 1
                    ind +=1
            ans.append("".join(nowL))

        return ans