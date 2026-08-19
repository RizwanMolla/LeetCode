from typing import List
import re

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid_lines = ["electronics", "grocery", "pharmacy", "restaurant"]
        line_priority = {line: idx for idx, line in enumerate(valid_lines)}
        
        valid_coupons = []
        
        for c, b, active in zip(code, businessLine, isActive):
            # Check active
            if not active:
                continue
            
            # Check business line
            if b not in line_priority:
                continue
            
            # Check code validity (non-empty, alphanumeric + underscore)
            if not c or not re.fullmatch(r"[A-Za-z0-9_]+", c):
                continue
            
            valid_coupons.append((b, c))
        
        # Sort by business line priority, then by code
        valid_coupons.sort(key=lambda x: (line_priority[x[0]], x[1]))
        
        # Return only the codes
        return [c for _, c in valid_coupons]
