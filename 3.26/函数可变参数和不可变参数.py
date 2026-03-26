a = (10,20,30,[10,20,30])
def test(n):
    n= (20,30,40,[100,200,300])
    print(n)
    n[3][0] = 200
    print(n)
test(a)
print(a)