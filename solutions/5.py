while 1:
 a=input()
 if len(a)<1:break
 x,y=a.split()
 w,z=x[::-1],y[::-1]
 if x[0]=="-":
  w="-"+w[:-1]
 if y[0]=="-":
  z="-"+z[:-1]
 print(z if float(z)>float(w) else w)