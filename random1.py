import random
n=random.randbytes(3)
print(n)
print(random.randrange(1,8))
print(random.randint(100,211))
mylist=["valaboju","shiva","kumar","chary"]
#mylist1={"valaboju","shiva","kumar","chary"}
mylist2={"valaboju":"shiva","kumar":"chary"}
#print(random.choice(mylist))
print(random.choice(list(mylist2.items())))
random.shuffle(mylist)
print(mylist)
