class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        n = len(s)

        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        matched = 0

        for i in range(n):
            x = ord(target[i]) - 97

            if cnt[x] > 0:
                cnt[x] -= 1
                matched += 1
            else:
                for j in range(i, -1, -1):
                    if j < i:
                        prev = ord(target[j]) - 97
                        cnt[prev] += 1

                    x = ord(target[j]) - 97

                    for c in range(x + 1, 26):
                        if cnt[c] > 0:
                            cnt[c] -= 1

                            result = list(target[:j])
                            result.append(chr(c + 97))

                            for k in range(26):
                                result.extend(
                                    [chr(k + 97)] * cnt[k]
                                )

                            return ''.join(result)

                return ""

        cnt = [0] * 26

        for i in range(n - 1, -1, -1):
            x = ord(target[i]) - 97
            cnt[x] += 1

            for c in range(x + 1, 26):
                if cnt[c] > 0:
                    cnt[c] -= 1

                    result = list(target[:i])
                    result.append(chr(c + 97))

                    for k in range(26):
                        result.extend(
                            [chr(k + 97)] * cnt[k]
                        )

                    return ''.join(result)

        return ""