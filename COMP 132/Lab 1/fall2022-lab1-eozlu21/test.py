import time

a = time.time()
x = 1
for i in range(10000):
    x += 1
    for k in range(10000):
        x -= 1
        for j in range(10000):
            x = 1
b = time.time()
print(a)
print(b)
print(b-a)
print(x)