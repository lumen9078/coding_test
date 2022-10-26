N = int(input())
x = list(map(int, input().split()))

cnt = 0
for i in x[:N]:
    if (i == 0) & (cnt != 0):
        N -= 1
        continue
    elif (i == 1) | (cnt == 0):
        cnt += N + (N - 1)
    elif i >= 2:
        cnt += len(str(i)) + 1
        cnt += N + (N - 1)
    cnt += 1    # +
    N -= 1

if x[-1] != 0:
    cnt += len(str(x[-1]))
else:
    cnt -= 1
cnt += 1    # =

print(cnt)