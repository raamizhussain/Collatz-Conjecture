c0 = int(input())
steps = 0
while c0 != 1:
    if c0%2 == 0:
        c0 = c0/2
        print(int(c0))
        steps += 1

        
    else:
        c0 = 3 * c0 + 1
        print(int(c0))
        steps += 1

print(f"Steps = {steps}")