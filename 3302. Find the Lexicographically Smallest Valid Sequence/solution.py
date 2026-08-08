class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        length1 = len(word1)
        length2 = len(word2)

        next_pos = [-1] * length2
        target = length2 - 1

        for index in range(length1 - 1, -1, -1):
            if target >= 0 and word1[index] == word2[target]:
                next_pos[target] = index
                target -= 1

        answer = []
        changed = False
        target_index = 0

        for index, char in enumerate(word1):
            if target_index >= length2:
                break

            matches = char == word2[target_index]
            can_change = (
                not changed
                and (
                    target_index == length2 - 1
                    or index < next_pos[target_index + 1]
                )
            )

            if matches or can_change:
                if not matches:
                    changed = True

                answer.append(index)
                target_index += 1

        return answer if target_index == length2 else []