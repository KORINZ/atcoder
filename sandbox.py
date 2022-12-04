dance = []
M = 3
for _ in range(M):
    k, *x = map(int, input().split())
    dance.append(set(x))

print(dance)
print(k)