n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
answer = []

for a in l:
    cnt = 0
    
    for b in l:
        if a[0] < b[0] and a[1] < b[1]:
            cnt += 1
            
    answer.append(cnt+1)

print(*answer)