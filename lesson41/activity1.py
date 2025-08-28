def soumilnikeshaadhya(x,y):
    z = 'alien'
    print("hi this is the code within the function, notice the blank space in the left, it is called as indentation")
    x = x + 2 * 4
    y = y/x * 2
    print(x+y)
    print(x*y)
    print(x/y)
    return z


print("this is outside the function")

zoutside = soumilnikeshaadhya(10, 2)
print('printing zoutside', zoutside)

def footballplayers(p1, p2):
    z = 'goal'
    print("R9 Ronaldo is the real phenomenon, a legend in football history!")
    p1 = p1 + " Messi"
    p2 = p2 + " Ronaldo"
    print("First Player:", p1)
    print("Second Player:", p2)
    print(p1 + " vs " + p2)
    return z


print("this is outside the function")

zoutside = footballplayers("Captain", "Striker")
print('printing zoutside', zoutside)

def chennai(x):
    if x == 1:
        print(x)
        return
    print(x)
    print("calling chennai with x-1")
    chennai(x-1)
    print("returning from chennai")

chennai(5)

