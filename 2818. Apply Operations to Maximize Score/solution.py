import sys
import math

class Solution:
    def maximumScore(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        max_num = max(nums) if nums else 0
        spf = [0] * (max_num + 1)
        for i in range(2, max_num + 1):
            if spf[i] == 0:
                spf[i] = i
                for j in range(i * i, max_num + 1, i):
                    if spf[j] == 0:
                        spf[j] = i
        
        def get_prime_score(x):
            if x == 1:
                return 0
            primes = set()
            while x > 1:
                p = spf[x]
                primes.add(p)
                while x % p == 0:
                    x = x // p
            return len(primes)
        
        prime_scores = [get_prime_score(num) for num in nums]
        
        left = [-1] * n
        stack = []
        for i in range(n):
            while stack and prime_scores[stack[-1]] < prime_scores[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            else:
                left[i] = -1
            stack.append(i)
        
        right = [n] * n
        stack = []
        for i in range(n-1, -1, -1):
            while stack and prime_scores[stack[-1]] <= prime_scores[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            else:
                right[i] = n
            stack.append(i)
        
        counts = []
        for i in range(n):
            l = i - left[i]
            r = right[i] - i
            counts.append(l * r)
        
        elements = []
        for i in range(n):
            elements.append((-nums[i], counts[i]))
        
        elements.sort()
        
        res = 1
        remaining_k = k
        for num_neg, cnt in elements:
            num = -num_neg
            if remaining_k <= 0:
                break
            take = min(cnt, remaining_k)
            res = (res * pow(num, take, MOD)) % MOD
            remaining_k -= take
        
        return res