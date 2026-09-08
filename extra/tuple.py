#tuple
tup1=('physics','chemistry',1997,2000)
tup2=(1,2,3,4,5,6,7)

print('tup1[0]:',tup1[0])
print('tup1[1:5]:',tup2[1:5])

#delete

tup=('phy','chem',1996,2010)

print(tup)
del tup;
print('After deleting tuple')

#basic operation in tuple

tup3=(1,2,3,4)
print(len(tup3))

tup4=(5,6,7,8)
print((1,2,3,4)+(5,6,7,8))

#repetition

tup5=('hi',)*4
print(tup5)

#membership

print(3 in (1,2,3,4))

for x in (1,2,3,4):
    print(x,end='')

