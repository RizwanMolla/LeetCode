class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        res = [-1, -1]

        mn = float("inf")

        prev = head
        cur = head.next
        idx = 1
        prev_cp = 0
        first_cp = 0

        while cur.next is not None:
            if (
                cur.val < prev.val and cur.val < cur.next.val
            ) or (
                cur.val > prev.val and cur.val > cur.next.val
            ):

                if prev_cp == 0:
                    prev_cp = idx
                    first_cp = idx
                else:
                    mn = min(mn, idx - prev_cp)
                    prev_cp = idx

            idx += 1
            prev = cur
            cur = cur.next

        if mn != float("inf"):
            mx = prev_cp - first_cp
            res = [mn, mx]

        return res