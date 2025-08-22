def removeStars(s: str) -> str:

  stack=[]
  for ch in s:
      if ch=="*":
          stack.pop()
      else:
          stack.append(ch)
  return "".join(stack)

s="lee**co*e"
print(removeStars(s))