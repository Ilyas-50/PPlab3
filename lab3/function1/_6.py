def func(str):
    arr = str.split()
    arr.reverse()
    for i in arr:
        print(i, end=" ")
    
inp = func(input())