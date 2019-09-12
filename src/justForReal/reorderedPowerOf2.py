from collections import Counter
class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        b = Counter(str(N))
        lb = len(str(N))
        power = 1
        while(True):
            la = len(str(power))
            if la<lb:
                power = power*2
                continue
            elif la>lb:
                break
            else:
                if Counter(str(power)) == b:
                    return True
                else:
                    power = power*2
                    continue
        return False