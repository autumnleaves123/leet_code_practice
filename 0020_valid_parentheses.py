class Solution:
    def isValid(self, s: str) -> bool:

        # completed on 3/22/2023

        bracket_type = ["(","{","["]
        opposite = { ")":"(","}":"{","]":"["}
        brackets = []

        for i in range(len(s)):
            character = s[i]
            if character in bracket_type:
                brackets.append(character)
            elif character in opposite:
                try:
                    if brackets[-1] == opposite[character]:
                        brackets.pop(-1)
                    else:
                        return False
                except:
                    return False
        return len(brackets) == 0
