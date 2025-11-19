def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        if n > 20:
            print("input too large")
            continue
        
        # compute factorial
        result = 1
        for i in range(1, n + 1):
            result *= i
        
        print(result)