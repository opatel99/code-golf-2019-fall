while 1:
 x = input()
 if len(x)<1:break
 a = ''
 b = ''
 for i in x:
  if i != " ":
   a = a + str(i.isupper()*1)
  if len(a) == 5:
   b=b+(chr(ord('A') + int(a,2)))
   a = ''
 print(b)