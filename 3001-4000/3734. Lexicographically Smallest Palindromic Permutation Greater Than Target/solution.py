class Solution:
    def lexPalindromicPermutation(self, text: str, bound: str) -> str:
        length = len(text)

        if length == 1:
            return text if text > bound else ""

        freq = [0] * 26
        for ch in text:
            freq[ord(ch) - ord("a")] += 1

        middle = ""
        for idx in range(26):
            if freq[idx] % 2:
                if middle:
                    return ""
                middle = chr(ord("a") + idx)
            freq[idx] //= 2

        left_part = []

        def is_greater(ch):
            candidate = left_part.copy()
            candidate.append(ch)

            for idx in range(25, -1, -1):
                candidate.extend([chr(ord("a") + idx)] * freq[idx])

            result = candidate + [middle] + candidate[::-1]
            return "".join(result) > bound

        for pos in range(length // 2):
            chosen = False

            for idx in range(26):
                if freq[idx] == 0:
                    continue

                freq[idx] -= 1

                if is_greater(chr(ord("a") + idx)):
                    left_part.append(chr(ord("a") + idx))
                    chosen = True
                    break
                else:
                    freq[idx] += 1

            if not chosen:
                return ""

            if left_part[pos] > bound[pos]:
                remaining = left_part[:]

                for idx in range(26):
                    remaining.extend(
                        [chr(ord("a") + idx)] * freq[idx]
                    )

                palindrome = remaining + [middle] + remaining[::-1]
                return "".join(palindrome)

        answer = left_part + [middle] + left_part[::-1]
        return "".join(answer)
