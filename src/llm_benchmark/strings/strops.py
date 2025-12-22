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
        """
        if not isinstance(s, str):
            raise TypeError(f"Parameter 's' must be a string, got {type(s).__name__}")
        
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
        """
        if not isinstance(s, str):
            raise TypeError(f"Parameter 's' must be a string, got {type(s).__name__}")
        
        for i in range(len(s)):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True
