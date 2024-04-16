class Solution(object):
    def lemonadeChange(self, bills):
        f, ten, t = 0, 0, 0

        for bill in bills:
            if bill == 5:
                f += 1
            elif bill ==10:
                if f > 0:
                    ten += 1
                    f -= 1
                else:
                    return False
            else:   
                if bill == 20 and f > 0 and ten > 0:
                        f -= 1
                        ten -= 1
                        t += 1
                elif bill == 20 and f >= 3:
                        f -=3
                        t +=1
                else:    
                        return False

        return True