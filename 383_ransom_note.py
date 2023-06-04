# https://leetcode.com/problems/ransom-note/

class RansomNote:
    def can_construct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        mag = magazine
        for letter in ransomNote:
            if letter in mag:
                mag = mag.replace(letter, '', 1)
            else:
                return False

        return True
