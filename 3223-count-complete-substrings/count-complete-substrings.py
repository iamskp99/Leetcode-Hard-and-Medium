import sys
input = sys.stdin.readline
class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:
        mat = [[] for i in range(26)]
        l = []
        n = len(word)
        d = {}
        adj = []
        z = -1
        cc = set()
        for e in range(n):
            i = word[e]
            ele = ord(i)-97
            cc.add(ele)
            if len(adj) == 0:
                adj.append(0)

            else:
                if abs(ele-z) > 2:
                    adj.append(adj[-1]+1)

                else:
                    adj.append(adj[-1])

            z = ele
            l.append(ele)
            if len(mat[0]) == 0:
                for j in range(26):
                    mat[j].append(0)

                mat[ele][-1] = 1
                d[(ele,mat[ele][-1])] = e

            else:
                for j in range(26):
                    mat[j].append(mat[j][-1])

                mat[ele][-1] += 1
                d[(ele,mat[ele][-1])] = e

        ans = 0
        for i in range(n):
            ele = l[i]
            qq = 0
            if i != 0:
                qq = adj[i]

            for j in cc:
                val = mat[j][i]
                if ele == j:
                    cur = val-1+k

                else:
                    cur = val+k

                ind = None
                if (j,cur) in d:
                    ind = d[(j,cur)]

                else:
                    continue

                if adj[ind]-qq > 0:
                    continue

                flag = True
                for g in cc:
                    if j == g:
                        continue

                    som = mat[g][ind]
                    if ele == g:
                        rom = som-mat[g][i]+1

                    else:
                        rom = som-mat[g][i]

                    if rom not in [0,k]:
                        flag = False
                        break

                if flag:
                    ans += 1

        return ans