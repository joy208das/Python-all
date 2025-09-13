
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    max_sum = -float('inf')
    
    for _ in range(n):
        max_sum = max(max_sum, a[0] + a[-1])
        a.insert(0, a.pop())
    
    print(max_sum)

t = int(input())
for _ in range(t):
    solve()