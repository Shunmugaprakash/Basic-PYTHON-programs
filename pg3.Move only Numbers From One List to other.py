lista=["shunmuga",234,"prakash",3422]
listb=[]
x=0
for item in lista:
  if isinstance(item,int):
     listb.append(item)
	 lista.pop(x)
   x+=1