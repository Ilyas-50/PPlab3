def filter_prime(arr):
    def check(n): #i can separate it to another function
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    for j in arr:
        if check(j):
            print(j , end= " ")

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
filter_prime(numbers)