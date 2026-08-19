from functools import lru_cache

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> list[int]:
        @lru_cache(None)
        def dfs(players: tuple, round_num: int):
            i, j = players.index(firstPlayer), players.index(secondPlayer)
            if i > j:
                i, j = j, i
            if i + 1 == len(players) - j:
                return (round_num, round_num)

            res = (float('inf'), -float('inf'))
            m = len(players)
            def gen_next(index, current):
                if index >= (m + 1) // 2:
                    yield current
                    return

                left = players[index]
                right = players[m - 1 - index]

                if left == right:
                    yield from gen_next(index + 1, current + [left])
                elif left in (firstPlayer, secondPlayer) or right in (firstPlayer, secondPlayer):
                    winner = left if left in (firstPlayer, secondPlayer) else right
                    yield from gen_next(index + 1, current + [winner])
                else:
                    yield from gen_next(index + 1, current + [left])
                    yield from gen_next(index + 1, current + [right])

            for next_players in gen_next(0, []):
                next_players_sorted = tuple(sorted(next_players))
                r1, r2 = dfs(next_players_sorted, round_num + 1)
                res = (min(res[0], r1), max(res[1], r2))

            return res

        players = tuple(range(1, n + 1))
        return list(dfs(players, 1))
