class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:

        def get_divs(num):
            # finds sum of non-trivial divisors of x (not 1, not x)
            # returns 0 if none found or more than one pair found
            divs = 0
            upper = isqrt(num) + 1
            i = 2
            while i < upper:
                if num % i == 0:
                    if num//i == i:
                        # a num w/ perfect squares can never have 4 divisors
                        return 0
                    if divs != 0:
                        # nums with > 4 divisors don't conttribute to sum
                        return 0
                    # sum of the 4 divisors
                    divs = i + num//i + 1 + num
                i += 1
            return divs

        # cache
        d = {}

        # sum
        s = 0

        for num in nums:
            t = d.get(num)
            if t is not None:
                s += t
                print(f"t for {num} is {t} (cached)")
            else:
                t = get_divs(num)
                print(f"t for {num} is {t} (computed)")
                d[num] = t
                s += t
        return s


                
        
