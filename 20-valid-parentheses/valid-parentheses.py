class Solution:
    def isValid(self, s: str) -> bool:
      closeToOpen = {
        "}":"{",
        "]":"[",
        ")":"("
      }

      stack = []
      for char in s:
        if char in closeToOpen.values():
            stack.append(char)
        elif char in closeToOpen.keys():
            if not stack or closeToOpen[char]!= stack.pop():
                return False
      return not stack
