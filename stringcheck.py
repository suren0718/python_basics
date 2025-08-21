def is_pangram(s):
  flag = 0
  for ch in s:
    flag |= 1<<(ord(ch)-ord('a'))

  return flag == (1<<26)-1

print(is_pangram("thequickbrownfoxjumpsoverthelazydog"))