T_cnt = int(input())

for cnt in range(T_cnt):
    case = list(map(int, input().split()))

    print("Case #%d: %d" % (cnt+1, case[0] + case[1]))
