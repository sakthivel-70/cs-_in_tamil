def palindrome(a):
  b=list(a)
  l=0
  r=len(b)-1
  while l<r:
    if b[l]!=b[r]:
      return False
    l+=1
    r-=1
  return True
print(palindrome("madam"))