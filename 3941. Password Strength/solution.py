class Solution:
    def passwordStrength(self, password: str) -> int:
        low = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
               "n","o","p","q","r","s","t","u","v","w","x","y","z"]

        up = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
              "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

        num = ["0","1","2","3","4","5","6","7","8","9"]

        sp = ["!","@","#","$"]

        strength = 0

        clow = set()
        cup = set()
        cnum = set()
        csp = set()

        for ch in password:
            if ch in low:
                clow.add(ch)

            elif ch in up:
                cup.add(ch)

            elif ch in num:
                cnum.add(ch)

            elif ch in sp:
                csp.add(ch)

        strength = (len(clow) * 1 +
                    len(cup) * 2 +
                    len(cnum) * 3 +
                    len(csp) * 5)

        return strength