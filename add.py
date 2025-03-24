def palindrome(a):
  b=list(a)
  l=0
  r=len(b)-1
  while l<r:
    if b[l]!=b[r]:
      return False
  return True
