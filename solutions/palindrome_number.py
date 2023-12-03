class PalindromeNumber:
    def is_palindrome_v1(self, x: int) -> bool:
        if x < 0:
            return False

        src = x
        dest = 0
        while src > 0:
            dest *= 10
            dest += src % 10
            src //= 10

        return x == dest

    def is_palindrome_v2(self, x: int) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True
        if x % 10 == 0:
            return False

        half = 0
        while x > half:
            half = half * 10 + x % 10
            x //= 10

        return x in (half, half // 10)
