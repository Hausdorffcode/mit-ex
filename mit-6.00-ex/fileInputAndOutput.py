f = open('test.txt', 'r')
#for line in f:
    #print line[0]
##f.close()


c = f.read(1)
while len(c) > 0:
    if len(c.strip()) > 0: print c,
    c = f.read(1)


file1 = open("TestFile.txt","w")
for i in range(1,10+1):
  print >>file1, i
file1.close()


file1 = open("TestFile.txt","a")
for i in range(1,10+1):
  if i>1:
    file1.write("-")
  file1.write(str(i))
file1.close()
