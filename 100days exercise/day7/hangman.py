nums = [2,7,11,15]
target = 9
r=0
for i in nums:

    r+=i
    if r==target:
        print("win")
print(r)