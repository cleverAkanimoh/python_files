n=5
while n>=1:
    print(n)
    n-=1

print("Blastoff!")
print("off to mars?")

def countdown():
    i=5
    while i>0:
        yield i
        i-=1
        
for i in countdown():
    print(i)