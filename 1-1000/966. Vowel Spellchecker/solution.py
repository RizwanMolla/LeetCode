from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        vowels = set("aeiou")

        def devowel(word: str) -> str:
            """Replace vowels with * and return lowercase version."""
            return "".join('*' if ch in vowels else ch for ch in word.lower())

        # Rule 1: Exact words
        wordset = set(wordlist)

        # Rule 2: Case-insensitive map (store first occurrence)
        case_map = {}
        # Rule 3: Vowel-error map (store first occurrence)
        vowel_map = {}

        for word in wordlist:
            lower = word.lower()
            if lower not in case_map:
                case_map[lower] = word
            v = devowel(lower)
            if v not in vowel_map:
                vowel_map[v] = word

        ans = []
        for q in queries:
            if q in wordset:  # Rule 1
                ans.append(q)
            elif q.lower() in case_map:  # Rule 2
                ans.append(case_map[q.lower()])
            elif devowel(q) in vowel_map:  # Rule 3
                ans.append(vowel_map[devowel(q)])
            else:
                ans.append("")  # No match
        return ans
