class StrOps:
    @staticmethod
    def str_reverse(s: str) -> str:
        """Reverse a string

        Args:
            s (str): String to reverse

        Returns:
            str: Reversed string

        Raises:
            TypeError: If s is not a string

        Note:
            Empty strings are valid inputs and will return an empty string.
        """
        if not isinstance(s, str):
            raise TypeError("Input must be a string")
        
        ret = ""
        for i in range(len(s)):
            ret += s[len(s) - 1 - i]
        return ret

    @staticmethod
    def palindrome(s: str) -> bool:
        """Check if a string is a palindrome

        Args:
            s (str): String to check

        Returns:
            bool: True if the string is a palindrome, False otherwise

        Raises:
            TypeError: If s is not a string

        Note:
            Empty strings are considered palindromes and will return True.
        """
        if not isinstance(s, str):
            raise TypeError("Input must be a string")
        
        for i in range(len(s)):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True
