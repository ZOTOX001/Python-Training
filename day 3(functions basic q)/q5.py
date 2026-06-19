# Show difference between local and global variables:
x = 100

def test():
    x = 50
    print("Local:", x)

test()
print("Global:", x)