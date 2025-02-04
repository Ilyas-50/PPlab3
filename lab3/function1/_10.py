def func(arr):
    uniq = []
    for i in arr:
        if i not in uniq:
            uniq.append(i)
    return uniq

print(func([0,1,1,2,5,8,6,3,2,1,1]))